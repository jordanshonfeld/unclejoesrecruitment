from django.contrib import admin
from django.urls import re_path, include
from . import views

app_name = 'applicants'

urlpatterns = [
    re_path(r'^$',views.applicant_home, name = 'app_home'),
    re_path(r'^register/$', views.applicant_register, name = 'register'), 
    re_path(r'^login/$', views.applicant_login, name = 'login'),
    re_path(r'^application/$', views.application, name = 'application'),
    re_path(r'^status_center/$', views.status_center, name = 'status_center')
]
