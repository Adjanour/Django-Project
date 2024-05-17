# views.py
import base64
import requests
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Payment
from .forms import PaymentForm
from django.http import HttpResponse
from .utils import format_phone_number


def initiate_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            mobile_number = format_phone_number(form.cleaned_data['mobile_number'])
            print(mobile_number)
            amount = form.cleaned_data['amount']
            title = "Payment Title"
            description = "Payment Description"
            client_reference = "your_unique_reference"
            callback_url = request.build_absolute_uri('/payment/callback/')
            cancellation_url = request.build_absolute_uri('/payment/cancellation/')
            return_url = request.build_absolute_uri('/payment/return/')
            logo_url = "https://www.adjarnor.tech/assets/IMG-20230804-WA0065-removebg-S8oLlPrF.png"

            # Basic Auth
            auth_string = f'{settings.HUBTEL_API_KEY}:{settings.HUBTEL_API_SECRET}'
            auth_encoded = base64.b64encode(auth_string.encode()).decode()

            # Hubtel API URL
            url = f'https://devp-reqsendmoney-230622-api.hubtel.com/request-money/{mobile_number}'
            url2 = f'https://devp-reqsendmoney-230622-api.hubtel.com/send-money/{mobile_number}'
            # Request Payload
            payload = {
                "amount": int(amount),
                "title": title,
                "description": description,
                "clientReference": client_reference,
                "callbackUrl": callback_url,
                "cancellationUrl": cancellation_url,
                "returnUrl": return_url,
                "logo": logo_url
            }
            print(payload)

            # Sending the request
            response = requests.post(
                url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Basic {auth_encoded}'
                },
                json=payload
            )
            response2 = requests.post(
                url2,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Basic {auth_encoded}'
                },
                json=payload
            )

            if response.status_code == 200:
                data = response.json()
                # Handle successful response
                return JsonResponse(data)
            else:
                # Handle errors
                return JsonResponse(response.json(), status=response.status_code)
    else:
        form = PaymentForm()
    return render(request, 'initiate_payment.html', {'form': form})


def payment_callback(request):
    # Handle the callback from Hubtel
    # You can update the payment status in your database here
    return HttpResponse('Callback received')


def payment_cancellation(request):
    # Handle the cancellation
    return HttpResponse('Payment cancelled')


def payment_return(request):
    # Handle the return
    return HttpResponse('Payment completed')
