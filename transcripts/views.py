# views.py
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import DeliveryOption, StudentProfile, TranscriptType
from .forms import TranscriptRequestForm
from .models import TranscriptRequest
from django.contrib.auth.decorators import login_required

@login_required
def transcript_request_view(request):
    # check if users profile is verified
    user = request.user
    profile = StudentProfile.objects.get(user=user)
    if not profile.is_verified:
        return redirect('profile')
    if request.method == 'POST':
        form = TranscriptRequestForm(request.POST)
        if form.is_valid():
            transcript_request = form.save(commit=False)
            transcript_request.user = request.user
            transcript_request.profile = StudentProfile.objects.get(user=request.user)
            transcript_request.total_cost = transcript_request.number_of_transcripts * 10  # Example cost calculation
            transcript_request.status = 'PENDING'
            transcript_request.save()

            # Initialize payment
            return redirect('initiate_payment', request_id=transcript_request.id)
    else:
        form = TranscriptRequestForm()
    delivery_options = list(DeliveryOption.objects.all().values('id', 'name', 'price'))
    transcript_types = list(TranscriptType.objects.all().values('id', 'name', 'price'))
    return render(request, 'transcript_request.html', {'form': form, 'delivery_options': delivery_options, 'transcript_types': transcript_types})


@login_required
def transcript_request_history_view(request):
    transcript_requests = TranscriptRequest.objects.prefetch_related('profile').filter(user=request.user).order_by('-created_at')
    return render(request, 'transcript_request_history.html', {'transcript_requests': transcript_requests})

@login_required
def edit_transcript_request_view(request, request_id=None):
    # check if users profile is verified
    user = request.user
    profile = StudentProfile.objects.get(user=user)
    if not profile.is_verified:
        return redirect('profile')
    
    transcript_request = get_object_or_404(TranscriptRequest, id=request_id)
    if request.method == 'POST':
        form = TranscriptRequestForm(request.POST, instance=transcript_request)
        if form.is_valid():
            transcript_request = form.save(commit=False)
            transcript_request.user = request.user
            transcript_request.profile = StudentProfile.objects.get(user=request.user)
            transcript_request.total_cost = transcript_request.number_of_transcripts * 10  # Example cost calculation
            transcript_request.status = 'PENDING'
            transcript_request.save()

            # Initialize payment
            return redirect('initiate_payment', request_id=transcript_request.id)
        # if form.is_valid():
        #     form.save()
        #     return redirect('transcript_request_history')
    elif request.method == 'GET':
        form = TranscriptRequestForm(instance=transcript_request)
        transcript_request = get_object_or_404(TranscriptRequest, id=request_id)
        return render(request, 'edit_transcript_request.html', {'form': form, 'transcript_request': transcript_request})
    

@login_required
def transcript_status_view(request):
    if request.method == 'GET':
        # Assuming you have a model TranscriptRequest to track transcript requests
        user = request.user
        transcript_requests = TranscriptRequest.objects.filter(user=user).order_by('-created_at')
        return render(request, 'transcript_status.html', {'transcript_requests': transcript_requests})


@login_required
def bulk_process_requests(request):
    if request.method == "POST":
        request_ids = request.POST.getlist('request_ids')
        for request_id in request_ids:
            transcript_request = TranscriptRequest.objects.get(id=request_id)
            transcript_request.status = 'processing'
            transcript_request.save()
        return redirect('admin_dashboard')
    return render(request, 'admin/bulk_process.html', {'requests': TranscriptRequest.objects.filter(status='pending')})
