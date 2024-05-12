from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class HomePageView(TemplateView):
 template_name = "home.html"




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form.fields.values)
        if form.is_valid():
            form.save()
            return redirect('account_login')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
