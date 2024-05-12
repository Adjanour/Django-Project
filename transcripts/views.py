from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import RegistrationForm

class HomePageView(TemplateView):
 template_name = "home.html"



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Success message or redirect to login page
            return redirect('login')  
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
