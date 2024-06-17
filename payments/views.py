# views.py
import json
import requests
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from transcripts.models import TranscriptRequest


def initiate_payment_view(request, request_id):
    transcript_request = get_object_or_404(TranscriptRequest, id=request_id)
    amount = int(transcript_request.total_cost * 100)  # Convert to pesewas
    email = request.user.email

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": email,
        "amount": amount,
        "reference": f"TRANS_{transcript_request.id}",
        "callback_url": request.build_absolute_uri("/payments/callback/"),
    }

    response = requests.post(
        "https://api.paystack.co/transaction/initialize",
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 200:
        response_data = response.json()
        authorization_url = response_data["data"]["authorization_url"]
        return redirect(authorization_url)
    else:
        return JsonResponse({"error": "Error initializing payment"}, status=500)


def payment_callback_view(request):
    reference = request.GET.get("reference")

    headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}

    response = requests.get(
        f"https://api.paystack.co/transaction/verify/{reference}", headers=headers
    )

    if response.status_code == 200:
        response_data = response.json()
        if response_data["data"]["status"] == "success":
            transcript_request_id = int(reference.split("_")[1])
            transcript_request = get_object_or_404(
                TranscriptRequest, id=transcript_request_id
            )
            if response_data["data"]["amount"] == int(
                transcript_request.total_cost * 100
            ):
                transcript_request.payment_status = "PAID"
                transcript_request.status = "PROCESSING"
            transcript_request.save()
            return render(
                request,
                "payment_success.html",
                {"transcript_request": transcript_request},
            )
        else:
            return render(request, "payment_failure.html")
    else:
        return render(request, "payment_failure.html")


def payment_success_view(request):
    reference = request.GET.get("reference")

    transcript_request = TranscriptRequest.objects.get(id=reference.split("_")[1])

    return render(
        request, "payment_success.html", {"transcript_request": transcript_request}
    )


def payment_failure_view(request):
    return render(request, "payment_failure.html")
