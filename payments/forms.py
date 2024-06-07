# forms.py
from django import forms


class PaymentForm(forms.Form):
    mobile_number = forms.CharField(
        max_length=15,
        label='Mobile Number',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter mobile number'
        })
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Amount',
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter amount'
        })
    )
