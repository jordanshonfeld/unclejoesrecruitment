from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from applicants.models import Applicant
from .models import Active
from django.contrib.auth.decorators import login_required


# Create your views here
def active_login(request):
    if request.user.is_authenticated:
        user = request.user
        applicants = Applicant.objects.filter(user = user)
        if len(applicants) > 0:
            return redirect('/applicants/')
        return redirect('/actives/')
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            applicants = Applicant.objects.filter(user = user)
            actives = Active.objects.filter(user = user)
            if len(applicants) > 0:
                return redirect('/applicants/')
            elif len(actives) > 0:
                active = actives[0]
                login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/actives/')
        else:
            message = "Login Failed"  
    else:
        form = AuthenticationForm()
        message = "Welcome back, please login :)"
    return render(request, 'actives/login.html', {'form':form, 'message':message})

@login_required(login_url="/actives/login/")
def active_home(request):
    if request.user.is_authenticated:
        user = request.user
        applicants = Applicant.objects.filter(user = user)
        if len(applicants) > 0:
            return redirect('/applicants/')
    if request.method == 'POST':
        request.getlist('applicants')
    applicants = Applicant.objects.all()
    return render(request, 'actives/home.html', {'applicants':applicants})
    
            