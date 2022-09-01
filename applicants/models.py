from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    email = models.EmailField(max_length=100, unique= True)
    name = models.CharField(max_length = 200, default = "Uncle Joe")
    student_id = models.CharField(max_length = 6, unique = True, default = "xxxxxx")
    round1 = models.BooleanField(default=False)
    round2 = models.BooleanField(default=False)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def create(cls, user, email, name, student_id, year_in_school):
        applicant = cls(user=user, email=email, name=name, student_id=student_id, year_in_school=year_in_school)
        return applicant

    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_student_id(self):
        return self.student_id
    def get_points(self):
        return self.points
    def get_year_in_school(self):
        return self.year_in_school
    def __str__(self):
        return self.name


class WrittenApp(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, default = None)
    submited = models.BooleanField(default=False)
    q1response = models.TextField(max_length=400, null = True, blank=True)
    q2response = models.TextField(max_length=1500, null = True, blank=True)
    q3response = models.TextField(max_length=1500, null = True, blank=True)
    q4response = models.TextField(max_length=1500, null = True, blank=True)
    q5response = models.BooleanField(default=False, null = True, blank=True)
    q5elaboration = models.TextField(blank=True, null = True)
    scenarioquestions = models.TextField(max_length=1000, null = True, blank=True)
    scenariovalidation = models.TextField(max_length=1500, null = True, blank=True)

    #Add application questions here

    def create(cls, applicant, q1response, q2response, q3response, q4response, q5response, q5elaboration, scenarioquestions, scenariovalidation): #will need to get changed as questions are added
        writtenapp = cls(applicant = applicant, q1response = q1response, q2response = q2response, q3response = q3response, q4response = q4response, q5response = q5response, q5elaboration = q5elaboration, scenarioquestions = scenarioquestions, scenariovalidation = scenariovalidation)
        return writtenapp

    def get_q1response(self):
        return self.q1response
    def get_q2response(self):
        return self.q2response
    def get_q3response(self):
        return self.q3response
    def get_q4response(self):
        return self.q4response
    def get_q5response(self):
        return self.q5response
    def get_q5aresponse(self):
        return self.q5elaboration
    def get_sQresponse(self):
        return self.scenarioquestions
    def get_sVresponse(self):
        return self.scenariovalidation
    
    def edit_responses(self, r1): #make sure to put in other responses here
        self.q1response = r1
        return self
    # other helpful methods, get applicant, get responses, etc.