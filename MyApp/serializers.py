from rest_framework import serializers
from .models import *




class ApplicantEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantEducation
        fields = '__all__'




class ApplicantCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantCertification
        fields = '__all__'



class ApplicantIntershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantIntership
        fields = '__all__'





class ApplicantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicants
        fields = '__all__'





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['username','first_name','last_name','email']