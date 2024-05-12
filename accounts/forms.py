# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the User model (built-in or custom)

class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields  = (
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
