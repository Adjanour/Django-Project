# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TranscriptRequestForm
from accounts.models import StudentProfile

@login_required
def request_transcript(request):
    if request.method == 'POST':
        form = TranscriptRequestForm(request.POST)
        if form.is_valid():
            transcript_request = form.save(commit=False)
            transcript_request.user = request.user
            transcript_request.profile = StudentProfile.objects.get(user=request.user)
            transcript_request.save()
            return redirect('transcript_request_success')
    else:
        form = TranscriptRequestForm()
    return render(request, 'request_transcript.html', {'form': form})

@login_required
def transcript_request_success(request):
    return render(request, 'request_success.html')
