# admin_views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from accounts.models import StudentProfile
from transcripts.models import TranscriptRequest
from .forms import TranscriptTypeForm, GenderForm, ProgramForm, DeliveryOptionForm

@staff_member_required
def admin_dashboard(request):
    requests = TranscriptRequest.objects.all()
    profiles = StudentProfile.objects.all()

    # Statistics
    total_requests = requests.count()
    total_profiles = profiles.count()
    pending_requests = requests.filter(status='Pending').count()
    approved_requests = requests.filter(status='Approved').count()
    rejected_requests = requests.filter(status='Rejected').count()

    context = {
        'requests': requests,
        'profiles': profiles,
        'total_requests': total_requests,
        'total_profiles': total_profiles,
        'pending_requests': pending_requests,
        'approved_requests': approved_requests,
        'rejected_requests': rejected_requests,
    }
    return render(request, 'admin_dashboard.html', context)

@staff_member_required
def manage_transcript_types(request):
    if request.method == "POST":
        form = TranscriptTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TranscriptTypeForm()
    return render(request, 'manage_transcript_types.html', {'form': form})

@staff_member_required
def manage_genders(request):
    if request.method == "POST":
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = GenderForm()
    return render(request, 'manage_genders.html', {'form': form})

@staff_member_required
def manage_programs(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProgramForm()
    return render(request, 'manage_programs.html', {'form': form})

@staff_member_required
def manage_delivery_options(request):
    if request.method == "POST":
        form = DeliveryOptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = DeliveryOptionForm()
    return render(request, 'manage_delivery_options.html', {'form': form})

@staff_member_required
def process_transcript_request(request, request_id):
    transcript_request = get_object_or_404(TranscriptRequest, id=request_id)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "approve":
            transcript_request.status = "Approved"
        elif action == "reject":
            transcript_request.status = "Rejected"
        transcript_request.save()
        return redirect('admin_dashboard')
    return render(request, 'process_transcript_request.html', {'transcript_request': transcript_request})
