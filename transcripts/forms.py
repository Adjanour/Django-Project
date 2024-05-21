# forms.py
from django import forms
from .models import TranscriptRequest

class TranscriptRequestForm(forms.ModelForm):
    class Meta:
        model = TranscriptRequest
        fields = ['delivery_email', 'delivery_address', 'number_of_transcripts', 'transcript_type']
        widgets = {
            'delivery_email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Email'}),
            'delivery_address': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Delivery Address'}),
            'number_of_transcripts': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500', 'placeholder': 'Number of Transcripts'}),
            'transcript_type': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
           
