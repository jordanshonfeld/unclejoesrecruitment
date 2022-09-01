from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from applicants.models import Applicant

def homepage(request):
    if request.user.is_superuser:
        logout(request)
    if request.user.is_authenticated:
        user = request.user
        applicants = Applicant.objects.filter(user = user)
        # print("*************** " + len(applicants))
        if len(applicants) != 0:
            active_user = True
            applicant = applicants[0]
            name = applicant.get_name()
    else:
        active_user = False
        name = ""
    return render(request, 'home.html', {'active_user':active_user, 'name':name})

def logout_view(request):
    logout(request)
    return redirect('/')
