from django.db import models
from django.contrib.auth.models import User
from applicants.models import Applicant

# Create your models here.
class Active(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    email = models.EmailField(max_length=100, unique= True, default = "xxxxx@wustl.edu")
    name = models.CharField(max_length = 200, default = "Uncle Joe")
    round1_roster = models.ManyToManyField('applicants.Applicant', related_name="first_round_roster", null=True)
    round2_roster = models.ManyToManyField('applicants.Applicant', related_name= "second_round_roster",null=True)
    
    def create(cls, user, email, name, student_id, x_list):
        active = cls(user=user, email=email, name=name, student_id=student_id, x_list = x_list)
        return active
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def __str__(self):
        return self.name

class x_pair(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    active = models.ForeignKey(Active, on_delete=models.CASCADE)

    def __str__(self):
        return self.applicant.name + ',' + self.active.name

class round1_roster(models.Model):
    a1 = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="a1")
    a2 = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="a2")
    a3 = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="a3")
    # Etcetera


