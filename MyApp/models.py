from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class ApplicantEducation(models.Model):
    
    applicanted_id = models.IntegerField()
    degree = models.CharField(max_length=100)
    fiedl_of_specialization = models.CharField(max_length=200)
    institute_name = models.CharField(max_length=200)
    date_of_completion = models.DateField(default=True)






class ApplicantCertification(models.Model):
    
    applicant_id = models.IntegerField()
    certification_name = models.CharField(max_length=100)
    issuing_organizationn = models.CharField(max_length=100)
    issue_date = models.DateField(default=True)
    certificate = models.CharField(max_length=255)




class ApplicantIntership(models.Model):
    applicant_intership_id = models.IntegerField()
    comany_name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=50)
    start_date = models.DateField(default=True)
    end_date = models.DateField(default=True)
    description = models.TextField()
    intership_certificate = models.CharField(max_length=2558)





class Applicants(models.Model):
    User_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField(default=True)
    phone_number = models.CharField(max_length=20)
    martial_status = models.CharField(max_length=30)
    home_town = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=255)
    pincode = models.IntegerField()
    current_location = models.CharField(max_length=400)
    resume = models.CharField(max_length=255)
    preferred_job_type= models.CharField(max_length=100)
    preferred_job_location = models.CharField(max_length=255,null=True)
    total_years_of_experience = models.IntegerField()
    availability_to_join = models.CharField(max_length=20)
    work_permit_for_USA = models.BooleanField()
    langauages = models.CharField(max_length=255)
    about =  models.CharField(max_length=1000)








