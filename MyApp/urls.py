from django.urls import path
from .views import *
from .views import ApplicantEducationAPI,ApplicantIntership,ApplicantsAPI


urlpatterns = [
   path('get_applicant/<int:id>',applicanteducation,name='applicanteducation'), #  applicanteducation FUNC
   # path('update_applicant/<int:id>',update_education,name='update_education'),
   # path('delete_applicant/<int:id>',delete_education,name='delete_education'),
   # path('get/',ApplicantEducationAPI.as_view()),                       # applicanteducation CLASS BASED 
   path('get_cert/<int:id>',applicantcertifate,name='applicantcertifate'),   # applicantcertifate cmpte
   path('get_intership/<int:id>',ApplicantIntershipAPI.as_view()),  
   path('update_intership/<int:id>',ApplicantIntershipAPI.as_view()),
   path('get_data/<int:id>',ApplicantsAPI.as_view()),

]
