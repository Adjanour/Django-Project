from django.shortcuts import render
from .models import AuditLog
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from accounts.models import Gender, GraduateType, IdentificationType, Programme, TranscriptType, DeliveryOption
from .forms import GenderForm, GraduateTypeForm, IdentificationTypeForm, ProgramForm, TranscriptTypeForm, DeliveryOptionForm

# Create your views here.
def log_action(user, action, transcript_request):
    AuditLog.objects.create(user=user, action=action, transcript_request=transcript_request)
    


@login_required
# @permission_required('is_staff')
def setup_view(request):
    
    genders = Gender.objects.all()
    programs = Programme.objects.all()
    transcript_types = TranscriptType.objects.all()
    delivery_options = DeliveryOption.objects.all()
    identification_types = IdentificationType.objects.all()
    graduate_types = GraduateType.objects.all()
    return render(request, 'setup.html', {
        'genders': genders,
        'programs': programs,
        'transcript_types': transcript_types,
        'delivery_options': delivery_options,
        'identification_types': identification_types,
        'graduate_types': graduate_types
    })

def add_gender(request):
    if request.method == 'POST':
        form = GenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup_view')
    else:
        form = GenderForm()
    return render(request, 'add_gender.html', {'form': form})

def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup_view')
    else:
        form = ProgramForm()
    return render(request, 'add_program.html', {'form': form})

def add_transcript_type(request):
    if request.method == 'POST':
        form = TranscriptTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup_view')
    else:
        form = TranscriptTypeForm()
    return render(request, 'add_transcript_type.html', {'form': form})

def add_delivery_option(request):
    if request.method == 'POST':
        form = DeliveryOptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup_view')
    else:
        form = DeliveryOptionForm()
    return render(request, 'add_delivery_option.html', {'form': form})

def add_identification_type(request):
    if request.method == 'POST':
        form = IdentificationTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup_view')
    else:
        form = IdentificationTypeForm()
    return render(request, 'add_identification_type.html', {'form': form})

def add_graduate_type(request):
    if request.method == 'POST':
        form = GraduateTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup_view')
    else:
        form = GraduateTypeForm()
    return render(request, 'add_graduate_type.html', {'form': form})
