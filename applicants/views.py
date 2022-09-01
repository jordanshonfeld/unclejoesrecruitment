from operator import truediv
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.http import HttpResponse
from applicants.models import Applicant, WrittenApp
from django.contrib.auth.models import User
from django.db import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from datetime import *


# Create your views here.
@login_required(login_url="/applicants/login/")
def applicant_home(request):
    user = request.user
    applicants = Applicant.objects.filter(user = user)
    applicant = applicants[0]
    name = applicant.get_name()
    form = forms.RegisterApplicantForm
    return render(request, 'applicants/homepage.html', {'form':form, 'name':name})

def applicant_register(request):
    if request.user.is_authenticated:
        message = "It looks like you are already registered. If you would like to register someone else please logout first."
        # Need to figure out how to make sure user knows why its being redirected
        return redirect('/applicants/')
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        applicant_form = forms.RegisterApplicantForm(request.POST)

        if user_form.is_valid() and applicant_form.is_valid():
            user = user_form.save()
            login(request,user)
            current_user = request.user
            applicant_form.save(commit=False)
            applicant = Applicant.create(Applicant, current_user, applicant_form['email'].value(), applicant_form['name'].value(), applicant_form['student_id'].value(), applicant_form['year_in_school'].value())
            email = applicant_form['email'].value()
            name = applicant_form['name'].value()

            applicant.save()
            print("applicant saved")
            subject = 'Welcome to UJ Application Portal'
            message = f'Hi {name}, \n\nThank you for registering for the Uncle Joes Application! Please use this platform to complete your application and check back for important updates.\n\nFor any problems that arise with the webiste please email unclejoesrecruitment@gmail.com. \n \nWe look forward to getting to know you throughout this process!\n \nBest, \nCarly and Jordan \nUncle Joes Recruitment Team'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('/applicants/')
        else:
            print("Register didn't work")
            print(user_form.errors)
            print(applicant_form.errors)
    else:
        user_form = UserCreationForm()
        applicant_form = forms.RegisterApplicantForm()
    return render(request, 'applicants/register.html', {'user_form':user_form, 'applicant_form':applicant_form})

def applicant_login(request):
    if request.user.is_authenticated:
        message = "It looks like you are already registered. If you would like to register someone else please logout first."
        return redirect('/applicants/', {'message':message})
        # Need to figure out how to make sure user knows why its being redirected
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            print("HERE 1 **********")
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                print("HERE 2**********")
                return redirect(request.POST.get('next'))
            else:
                print("HERE 3**********")
                return redirect('/applicants/')
        else:
            message = "Login Failed"  
    else:
        form = AuthenticationForm()
        message = "Welcome back, please login :)"
    return render(request, 'applicants/login.html', {'form':form, 'message':message})

@login_required(login_url="/applicants/login/")
def application(request):
    duedate = date(2022, 9, 27)
    now = date.today()
    overdue = False
    if now > duedate:
        overdue = True
        return render(request, 'applicants/application.html', {'overdue':overdue}) 
    user = request.user
    applicants = Applicant.objects.filter(user = user)
    applicant = applicants[0]
    name = applicant.get_name()
    apps = WrittenApp.objects.filter(applicant=applicant)
    if request.method == 'POST':
        form = forms.WrittenAppForm(request.POST)
        if form.is_valid():
            if len(apps)>0:
                writtenapp = apps[0]
                # writtenapp.edit_responses(form['q1response'].value())
                writtenapp.q1response = form['q1response'].value()
                writtenapp.q2response = form['q2response'].value()
                writtenapp.q3response = form['q3response'].value()
                writtenapp.q4response = form['q4response'].value()
                writtenapp.q5response = form['q5response'].value()
                writtenapp.q5elaboration = form['q5elaboration'].value()
                writtenapp.scenarioquestions = form['scenarioquestions'].value()
                writtenapp.scenariovalidation = form['scenariovalidation'].value()
                writtenapp.save()
            else:
                writtenapp = WrittenApp.create(WrittenApp, applicant, form['q1response'].value(), form['q2response'].value(), form['q3response'].value(), form['q4response'].value(), form['q5response'].value(), form['q5elaboration'].value(), form['scenarioquestions'].value(), form['scenariovalidation'].value())
                writtenapp.save()
            return redirect('/applicants/status_center/') #this should probably redirect to a status = completed page
            #there should also be options to save along the way......
    else:
        form = forms.WrittenAppForm()
        if len(apps) > 0:
            cur_app = apps[0]
            r1 = cur_app.get_q1response()
            r2 = cur_app.get_q2response()
            r3 = cur_app.get_q3response()
            r4 = cur_app.get_q4response()
            r5 = cur_app.get_q5response()
            r5a = cur_app.get_q5aresponse()
            sQ = cur_app.get_sQresponse()
            sV = cur_app.get_sVresponse()
            return render(request, 'applicants/application.html', {'name':name, 'form':form, 'r1':r1, 'r2':r2, 'r3':r3, 'r4':r4, 'r5':r5, 'r5a':r5a, 'sQ':sQ, 'sV':sV, 'overdue':overdue})
    return render(request, 'applicants/application.html', {'name':name, 'form':form, 'overdue':overdue})

    #add application questions here
    #eg, q1prompt = "why are butts so awesome"

@login_required(login_url="/applicants/login/")
def status_center(request):
    user = request.user
    applicants = Applicant.objects.filter(user = user)
    applicant = applicants[0]
    name = applicant.get_name()
    apps = WrittenApp.objects.filter(applicant=applicant)
    if len(apps):
        submitted = True
    else:
        submitted = False
        return render(request, 'applicants/status_center.html', {'name':name, 'submitted':submitted, 'applicant':applicant})
    #have info about rounds here too
    #have applicants be able to view their application
    return render(request, 'applicants/status_center.html', {'name':name, 'submitted':submitted, 'app':apps[0], 'applicant':applicant})
