from django import forms
from accounts.models import Gender, GraduateType, IdentificationType, Programme, TranscriptType, DeliveryOption


class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = ['name','short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Name'}),
            'short_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Short Name'}),
        }

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['name', 'short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Name'}),
            'short_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Short Name'}),
        }

class TranscriptTypeForm(forms.ModelForm):
    class Meta:
        model = TranscriptType
        fields = ['name','short_name','price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Name'}),
            'short_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Short Name'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Price'}),
        }

class DeliveryOptionForm(forms.ModelForm):
    class Meta:
        model = DeliveryOption
        fields = ['name', 'price', 'short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Name'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Price'}),
            'short_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Short Name'}),
        }

class IdentificationTypeForm(forms.ModelForm):
    class Meta:
        model = IdentificationType
        fields = ['name', 'short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Name'}),
            'short_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Short Name'}),
        }
        
class GraduateTypeForm(forms.ModelForm):
    class Meta:
        model = GraduateType
        fields = ['name', 'short_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Name'}),
            'short_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder:': 'Short Name'}),
        }