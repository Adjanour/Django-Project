# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import StudentProfile, CourseLog

User = get_user_model()  # Get the User model (built-in or custom)


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class RegistrationForm(forms.Form):
    class Meta:
        fields = ['username']

    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        if commit:
            user.save()
        return user


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('profile_image', 'first_name', 'last_name', 'other_names', 'email', 'gender', 'residential_address',
                  'postal_address', 'date_of_birth', 'phone_number')
        
    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.verification_status == 'PENDING':
            for field in self.fields:
                self.fields[field].disabled = True        


class StudentProfileFormID(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('identification_type', 'identification_number', 'identification_file')
        
        def __init__(self, *args, **kwargs):
            super(StudentProfileFormID, self).__init__(*args, **kwargs)
            if self.instance and self.instance.verification_status == 'PENDING':
                for field in self.fields:
                    self.fields[field].disabled = True


class StudentProfileFormProgramme(forms.ModelForm):
    class Meta:
        model = CourseLog
        fields = ('index_number', 'full_name', 'graduate_type', 'programme', 'admission_year', 'graduation_year')
        
        def __init__(self, *args, **kwargs):
            super(StudentProfileFormProgramme, self).__init__(*args, **kwargs)
            if self.instance and self.instance.verification_status == 'PENDING':
                for field in self.fields:
                    self.fields[field].disabled = True


class CourseLogForm(forms.ModelForm):
    class Meta:
        model = CourseLog
        fields = ['index_number', 'full_name', 'graduate_type', 'programme',
                  'admission_year', 'graduation_year']
        widgets = {
            'admission_year': forms.NumberInput(attrs={'min': 2000, 'max': 2050}),
            'graduation_year': forms.NumberInput(attrs={'min': 2000, 'max': 2050, 'required': False}),
        }
