from .forms import StudentProfileForm, StudentProfileFormID, CourseLogForm
from django.shortcuts import redirect
from .models import CourseLog


# def handle_course_log_forms(request, profile):
#     """
#   Processes multiple CourseLogForm submissions for a user's profile.
#
#   Args:
#       request (HttpRequest): The Django request object.
#       profile (object): The user's profile object.
#
#   Returns:
#       HttpResponseRedirect: Redirects to the profile view with the updated step
#                           if successful, otherwise returns None.
#   """
#     if request.method != 'POST':
#         return None
#
#     print(request.POST)
#     course_log_forms = []
#     course_log_form = CourseLogForm()  # Create an empty form to determine prefix length
#
#     course_log_forms = []
#     print("post length", len(request.POST))
#     length = (len(request.POST) - 2) // (len(course_log_form.fields) - 2) if (len(request.POST) - 2) // (
#                 len(course_log_form.fields) - 2) > 0 else 1
#     print("length", length)
#     for form_number in range(length):
#         form_data = {}
#         for field_name, field_values in request.POST.items():
#             print(field_name)
#             if field_name:  # Check prefix
#                 print(field_name.split('-')[0])
#                 form_data[field_name.split('-')[0]] = request.POST[field_name]  # Extract single value
#             print(form_data)
#
#         form = CourseLogForm(data=form_data)  # Create form with extracted data
#         if form.is_valid():
#             print("Form is valid")
#             cleaned_data = form.cleaned_data
#             cleaned_data['profile'] = profile  # Associate with user's profile
#             course_log_forms.append(cleaned_data)
#
#         else:
#             # Handle invalid form data (optional: store errors for template display)
#             print(f"Form {form_number} validation error: {form.errors}")
#             return None  # Indicate failure to process forms
#
#     # Process all valid course log data
#     for course_log_data in course_log_forms:
#         CourseLog.objects.create(**course_log_data)  # Efficient bulk creation
#
#     profile.step = 4  # Update user's profile step
#
#     profile.save()
#
#     return redirect('profile', step=profile.step)  # Redirect with updated step


def handle_course_log_forms(request, profile):
    """
    Processes multiple CourseLogForm submissions for a user's profile.

    Args:
        request (HttpRequest): The Django request object.
        profile (object): The user's profile object.

    Returns:
        HttpResponseRedirect: Redirects to the profile view with the updated step
                              if successful, otherwise returns None.
    """
    if request.method != 'POST':
        return None

    # Initialize an empty list to store cleaned data from valid forms
    course_log_forms = []
    # array to store index_number and full_name
    data = []
    temp_form = CourseLogForm()

    # Extract form prefixes
    prefixes = set()
    for key in request.POST.keys():
        if '-' in key:
            prefix = key.split('-')[0] + key.split('-')[1]
            prefixes.add(prefix)

    length = len(prefixes)
    print("length", length)
    print(request.POST)

    for form_number in range(1, length + 1):
        form_data = {}
        prefix = f'form-{form_number}'

        for field_name in temp_form.fields.keys():
            key = f'{prefix}-{field_name}'
            if key in request.POST:
                form_data[field_name] = request.POST[key]

        instance_id_key = f'{prefix}-id'
        if instance_id_key in request.POST:
            try:
                instance = CourseLog.objects.get(id=request.POST[instance_id_key], profile=profile)
            except CourseLog.DoesNotExist:
                instance = None
        else:
            instance = None

        try:
            if form_data['index_number'] and form_data['full_name']:
                data.append(form_data['index_number'])
                data.append(form_data['full_name'])
        except KeyError:
            pass

        form = CourseLogForm(data=form_data, instance=instance)
        # add index_number and full_name to form
        print(form.data)
        form.data['index_number'] = data[0]
        form.data['full_name'] = data[1]

        if form.is_valid():
            cleaned_data = form.save(commit=False)
            cleaned_data.profile = profile
            cleaned_data.save()
        else:
            print(form_data)
            print(f"Form {form_number} validation error: {form.errors}")
            return None  # Indicate failure to process forms

    profile.step = 4
    profile.save()

    return redirect('profile', step=profile.step)


def get_form(post, files, step, profile):
    print(step)
    if step == 1:
        return StudentProfileForm(post, files, instance=profile)
    elif step == 2:
        return StudentProfileFormID(post, files, instance=profile)
    elif step == 3:
        return CourseLogForm(post, files, instance=profile)
    elif step == 4:
        return StudentProfileForm(post, files, instance=profile)
    else:
        raise ValueError("Invalid step value")


def get_form_get(step, profile):
    print(step)
    if step == 1:
        return StudentProfileForm(instance=profile)
    elif step == 2:
        return StudentProfileFormID(instance=profile)
    elif step == 3:
        return CourseLogForm(instance=profile)
    elif step == 4:
        return StudentProfileForm(instance=profile)
    else:
        raise ValueError("Invalid step value")


def get_step_info(steps, profile_step):
    for step in steps:
        step['completed'] = step['number'] <= profile_step
        step['current'] = step['number'] == profile_step
    return steps
