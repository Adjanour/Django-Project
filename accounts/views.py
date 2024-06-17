from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from .forms import (
    RegistrationForm,
    StudentProfileForm,
    StudentProfileFormID,
    CourseLogForm,
)
from .models import (
    StudentProfile,
    IdentificationType,
    Gender,
    CourseLog,
    Programme,
    GraduateType,
)
from .utils import get_form, get_step_info, get_form_get, handle_course_log_forms


@login_required
def HomePageView(request):
    notifications = Notification.objects.filter(user=request.user).order_by("-date")
    notifications_count = notifications.count()
    return render(request, "home.html", {"notifications": notifications})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account_login")
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "register.html", context)


@login_required
def verify_student(request, student_pk):
    # Verification logic will be implemented here in the future
    pass


@login_required
def profile(request, step=1):
    user = request.user
    profile, created = StudentProfile.objects.get_or_create(user=user)
    last_completed_step = profile.step

    steps = get_step_info(
        [
            {"number": 1, "name": "Biodata"},
            {"number": 2, "name": "Identification"},
            {"number": 3, "name": "Programmes"},
            {"number": 4, "name": "Review"},
        ],
        profile.step,
    )

    # Redirect to last completed step if trying to access an invalid step
    if step > last_completed_step:
        return redirect("profile", step=last_completed_step)

    if request.method == "POST":
        if step == 3:
            result = handle_course_log_forms(request, profile)
            if result:
                return result  # Redirect to profile view with updated step
        form = get_form(request.POST, request.FILES, step, profile)

        if form.is_valid():

            if step == 2:
                if (
                    "identification_file" not in request.FILES
                    and profile.identification_file
                ):
                    form.cleaned_data["identification_file"] = (
                        profile.identification_file
                    )
                    print("Using existing identification file")

            form.save()
            profile.step = min(profile.step + 1, 4)  # Ensure step does not exceed 4
            profile.save()
            return redirect("profile", step=profile.step)
        else:
            print("Form validation error")
    else:
        if step == 3:
            return render_course_log_form(request, profile, steps, step)
        elif step == 4:
            return render_review_step(request, profile, steps, step)
        else:
            form = get_form_get(step, profile)

    context = {
        "form": form,
        "steps": steps,
        "id_types": IdentificationType.objects.all(),
        "step": step,
        "genders": Gender.objects.all(),
        "programmes": Programme.objects.all(),
        "graduate_types": GraduateType.objects.all(),
    }
    if profile.profile_image:
        context["profile_image_url"] = profile.profile_image.url
    return render(request, "profile.improved.html", context)


def render_course_log_form(request, profile, steps, step):
    all_programmes = Programme.objects.all()
    graduate_types = GraduateType.objects.all()
    existing_course_logs = CourseLog.objects.filter(profile=profile)
    course_log_forms = [
        CourseLogForm(instance=log, prefix=f"form-{i+1}")
        for i, log in enumerate(existing_course_logs)
    ]
    if not course_log_forms:
        course_log_forms.append(CourseLogForm(prefix="form-1"))

    context = {
        "steps": steps,
        "id_types": IdentificationType.objects.all(),
        "step": step,
        "course_log_forms": course_log_forms,
        "profile": profile,
        "programmes": all_programmes,
        "graduate_types": graduate_types,
    }
    return render(request, "profile.improved.html", context)


def render_review_step(request, profile, steps, step):
    course_logs = CourseLog.objects.filter(profile=profile)
    context = {
        "steps": steps,
        "id_types": IdentificationType.objects.all(),
        "step": step,
        "profile": profile,
        "course_logs": course_logs,
    }
    return render(request, "profile.improved.html", context)


@login_required
def submit_profile(request):
    user = request.user
    profile = StudentProfile.objects.get(user=user)
    profile.verification_status = "PENDING"
    profile.save()

    return redirect("/")
