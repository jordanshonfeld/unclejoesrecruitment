from django import forms
from .models import Applicant, WrittenApp
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class RegisterApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['email', 'name', 'student_id', 'year_in_school']
        labels = {
            'email':'WashU Email',
            'name': 'Full Name',
            'student_id':'Student ID',
            'year_in_school':'Year'
        }

class WrittenAppForm(forms.ModelForm):
    class Meta:
        model = WrittenApp
        fields = ['q1response','q2response','q3response','q4response','q5response','q5elaboration','scenarioquestions','scenariovalidation'] #obviously, this will need to change
    
    


# User = get_user_model()
# class RegisterApplicantForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput)
#     password_2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['email', 'year_in_school', 'firstName', 'lastName', 'student_id']
#         lables = {
#             'email':'WashU Email',
#             'year_in_school':"Year",
#             'firstName':'First Name',
#             'lastName':'Last Name',
#             'student_id':'Student ID'
#         }
#     def clean(self):
#         '''
#         Verify both passwords match.
#         '''
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "Your passwords must match")
#         return cleaned_data

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user

