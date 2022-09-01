# Register your models here.
from django.contrib import admin
from .models import Applicant, WrittenApp

admin.site.register(Applicant)

admin.site.register(WrittenApp)