from django.contrib import admin
from django.urls import re_path, include
from . import views

app_name = 'applicants'

urlpatterns = [
    re_path(r'^login/$', views.active_login, name = 'login'),
    re_path(r'^$', views.active_home, name = 'act_home' )
]
