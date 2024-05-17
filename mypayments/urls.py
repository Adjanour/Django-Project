# urls.py
from django.urls import path
from .views import initiate_payment, payment_callback, payment_cancellation, payment_return

urlpatterns = [
    path('payment/', initiate_payment, name='initiate_payment'),
    path('payment/callback/', payment_callback, name='payment_callback'),
    path('payment/cancellation/', payment_cancellation, name='payment_cancellation'),
    path('payment/return/', payment_return, name='payment_return'),
]
