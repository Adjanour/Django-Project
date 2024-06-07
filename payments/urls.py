# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('payments/initiate-payment/<int:request_id>/', views.initiate_payment_view, name='initiate_payment'),
    path('payments/callback/', views.payment_callback_view, name='payment_callback'),
    path('payments/success/', views.payment_success_view, name='payment_success'),
    path('payments/ailure/', views.payment_failure_view, name='payment_failure'),
]
