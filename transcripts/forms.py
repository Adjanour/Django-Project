# forms.py
from django import forms

from accounts.models import DeliveryOption, TranscriptType
from .models import TranscriptRequest

class TranscriptRequestForm(forms.ModelForm):
    class Meta:
        model = TranscriptRequest
        fields = ['delivery_email', 'delivery_address', 'number_of_transcripts', 'transcript_type', 'delivery_option']
        widgets = {
            'delivery_email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder': 'Email','required':'True'}),
            'delivery_address': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder': 'Delivery Address','required':'True'}),
            'number_of_transcripts': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder': 'Number of Transcripts','required':'True'}),
            'transcript_type': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder': 'Transcript Type','default':"Transcript Type",'required':'True'}),
            'delivery_option': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-green-500', 'placeholder': 'Delivery Option','required':'True'}),
        }
           
