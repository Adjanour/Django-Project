from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile, IdentificationType, Gender, CourseLog, Programme, GraduateType
from .forms import StudentProfileForm, StudentProfileFormID, CourseLogForm
from .utils import get_form, get_step_info, get_form_get, handle_course_log_forms


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
def profile(request, step=1):
    user = request.user
    profile = user.profile
    programmes = CourseLog.objects.filter(profile=profile)

    if profile is None:
        # Create a new profile if it doesn't exist
        profile = StudentProfile.objects.create()
        user.profile = profile
        user.save()
        profile = user.profile
        # Get the user's last completed step
    last_completed_step = profile.step

    steps = get_step_info([
        {'number': 1, 'name': 'Biodata'},
        {'number': 2, 'name': 'Identification'},
        {'number': 3, 'name': 'Programmes'},
        {'number': 4, 'name': 'Review'}
    ], profile.step)
    id_types = IdentificationType.objects.all()
    genders = Gender.objects.all()
    allProgrammes = Programme.objects.all()
    graduate_types = GraduateType.objects.all()

    # Check if requested step is valid based on last completed step
    if step > last_completed_step:
        return redirect('profile', step=last_completed_step)  # Redirect to last completed step

    if request.method == 'POST':
        if step == 3:
            print("Handling course log forms")
            result = handle_course_log_forms(request, profile)
            if result is None:
                pass
            else:
                return result  # Redirect to profile view with updated step
        form = get_form(request.POST, request.FILES, step, profile)
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
            form.save()
            if step == 1 and profile.step == 1:
                profile.step = 2
            elif step == 2 and profile.step == 2:
                profile.step = 3

            profile.save()
            return redirect('profile', step=profile.step)
        else:
            print("Form validation error")
    else:
        if step == 3:
            allProgrammes = Programme.objects.all()
            graduate_types = GraduateType.objects.all()

            # Get existing CourseLog entries for the profile
            existing_course_logs = CourseLog.objects.filter(profile=profile)

            # Create a list of forms pre-populated with existing data
            course_log_forms = [
                CourseLogForm(instance=course_log, prefix=f'form-{i+1}')
                for i, course_log in enumerate(existing_course_logs)
            ]

            # Add an empty form for adding a new CourseLog
            if len(course_log_forms) == 0:
                course_log_forms.append(CourseLogForm(prefix=f'form-{1}'))

            context = {'steps': steps, 'id_types': id_types, 'step': step, 'course_log_forms': course_log_forms,
                       'profile': profile, 'programmes': allProgrammes,
                       'graduate_types': graduate_types}
            return render(request, 'profile.improved.html', context)
        elif step == 4:
            profile = get_object_or_404(StudentProfile, customuser=request.user)
            course_logs = CourseLog.objects.filter(profile=profile)

            context = {
                'steps': steps, 'id_types': id_types, 'step': step,
                'profile': profile,
                'course_logs': course_logs
            }
            return render(request, 'profile.improved.html', context)
s        else:
            form = get_form_get(step, profile)

    context = {'form': form, 'steps': steps, 'id_types': id_types, 'step': step, 'genders': genders,
               'programmes': allProgrammes, 'graduate_types': graduate_types}
    return render(request, 'profile.improved.html', context)
