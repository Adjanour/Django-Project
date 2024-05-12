from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .models import StudentProfile
from .forms import StudentProfileForm  


class HomePageView(TemplateView):
 template_name = "home.html"




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.fields.values)
        if form.is_valid():
            form.save()
            return redirect('account_login')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)



@login_required
def verify_student(request, student_pk):
    pass
#   profile = StudentProfile.objects.get(pk=student_pk)
#   # Implement logic to verify or reject student based on documents
  
#   if verification_successful:
#     profile.verification_status = 'VERIFIED'
#     profile.save()
#     # Send verification email notification
#   else:
#     profile.verification_status = 'REJECTED'
#     profile.save()
#     # Send rejection email notification
#   return redirect('admin:transcript_app_studentprofile_changelist')  


@login_required
def profile(request):
    user = request.user
    print(user)
  
    profile = user.profile
    
    if profile is None:
        # Create a new profile if it doesn't exist
        profile = StudentProfile.objects.create()
        user.profile = profile
        user.save()
        profile = user.profile
        
        
        
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        print(form)
        print(form.is_valid())
        print(form.errors)
        print(form.cleaned_data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            pass
    else:
        form = StudentProfileForm(instance=profile)

    print(profile.step)
    print("getting here")
    # Determine step information
    steps = [
        {'number': 1, 'name': 'Biodata', 'completed': profile.step >= 1, 'current': profile.step == 1},
        {'number': 2, 'name': 'Identification', 'completed': profile.step >= 2, 'current': profile.step == 2},
        {'number': 3, 'name': 'Programmes', 'completed': profile.step >= 3, 'current': profile.step == 3},
        {'number': 4, 'name': 'Review', 'completed': profile.step >= 4, 'current': profile.step == 4}
    ]
    print(steps)
    context = {'form': form, 'steps': steps}
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    print(user)
    try:
        profile = user.profile
        print(profile)
    except:
        # Create a new profile if it doesn't exist
        # create profile and associate it to the user
        profile = StudentProfile.objects.create()
        user.profile = profile
        user.save()
    

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        print(form)
        if form.is_valid():
            form.save()
            # Success message or redirection 
            return redirect('edit_profile')
        else:
                # Error message
                pass
    else:
        form = StudentProfileForm(instance=profile)

    print(profile.step)
    print("getting here")
    steps = [
    {'number': 1, 'name': 'Biodata', 'completed': profile.step>=1,'current': profile.step==1},
    {'number': 2, 'name': 'Education', 'completed': profile.step>=2,'current': profile.step==2},
    {'number': 3, 'name': 'Documents', 'completed': profile.step>=3,'current': profile.step==3}
    ]
    print(steps)
    context = {'form': form, 'steps': steps}
    return render(request, 'profile.html', context)