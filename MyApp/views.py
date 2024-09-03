from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Applicants,ApplicantEducation,ApplicantIntership,ApplicantCertification,User
from .serializers import ApplicantEducationSerializer,ApplicantCertificationSerializer,ApplicantIntershipSerializer,ApplicantsSerializer,UserSerializer
from rest_framework.views import APIView

# Create your views here.




#  Applicant Education   Compelete

@api_view(["GET","POST","PUT","DELETE"])
def applicanteducation(request,id):
    
    if request.method == "GET":
        applicant_obj = ApplicantEducation.objects.all()
        serializer = ApplicantEducationSerializer(applicant_obj,many=True)
        return Response(serializer.data)
    
    
    
    if request.method == "POST":
        jsondata = request.data
        serializer = ApplicantEducationSerializer(data=jsondata)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Appliceducation added"})
        return Response({"message":"Not Added Appliceducation"})



# @api_view(["PUT"])
# def update_education(request,id):
    if request.method == "PUT":
        jsondata = request.data
        
        abc = ApplicantEducation.objects.get(id=id)
        serializer = ApplicantEducationSerializer(abc,data=jsondata)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Appliceducation update"})
        return Response({"message":"Not update Appliceducation"})
    

    if request.method == "DELETE":
        appicant_edu = ApplicantEducation.objects.get(id=id)
        appicant_edu.delete()
        return Response({"message":"Appliceducation Delete"})
    return Response({"message":"Not Delete Appliceducation"})


   




#  CLASS Based Views

class ApplicantEducationAPI(APIView):
    def get(self,request):
        applicant_obj = ApplicantEducation.objects.all()
        serializer = ApplicantEducationSerializer(applicant_obj,many=True)
        return Response(serializer.data)
    

    def post(self,request):

        data = request.data
        serializer = ApplicantEducationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"message":"new applicant class based"})
        return Response ({"message":"no added applicant"})
    

    def put(self,request,id=id):

        data = request.data
        applicant_obj = ApplicantEducation.objects.get(id=id)
        serializer = ApplicantEducationSerializer(applicant_obj,data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"update applicant"})
        return Response({"message":"Not update applicant"})
    





#  Application certification  CRUD compelete 

@api_view(["GET","POST","PUT","DELETE"])
def applicantcertifate(request,id):
    
    if request.method == "GET":
        applicant_certi = ApplicantCertification.objects.all()
        serializer = ApplicantCertificationSerializer(applicant_certi,many=True)
        return Response(serializer.data)
    
    
    if request.method == "POST":
        jsondata = request.data
        serializer = ApplicantCertificationSerializer(data=jsondata)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Appliceducation added"})
        return Response({"message":"Not Added Appliceducation"})
    


    if request.method == "PUT":
        jsondata = request.data
        
        abc = ApplicantCertification.objects.get(id=id)
        serializer = ApplicantCertificationSerializer(abc,data=jsondata)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"ApplicantCertificate update"})
        return Response({"message":"ApplicantCertificate Not updat"})
    


    if request.method == "DELETE":
        applicant_certi = ApplicantCertification.objects.get(id=id)
        applicant_certi.delete()
        
        return Response({"message":"Appliceducation Delete"})
    return Response({"message":"Not Delete Appliceducation"})




#  APPLICANT INTERSHIP    CRUD Complete 

class ApplicantIntershipAPI(APIView):
    def get(self,request,id):

        appli_inter = ApplicantIntership.objects.all()
        serializer = ApplicantIntershipSerializer(appli_inter,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        data = request.data
        serializer = ApplicantIntershipSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({"status":"200 successfully ADDED"})
        return Response({"status":"400"})
    


    def put(self,request,id):
        data = request.data
        appli_inter = ApplicantIntership.objects.get(id=id)
        serializer = ApplicantIntershipSerializer(appli_inter,data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"ApplicantIntership update"})
        return Response({"message":"ApplicantIntership Not update"})
    
    
    def delete(self,id):
        appli_inter = ApplicantIntership.objects.get(id=id)
        appli_inter.delete()
        return Response({"message":"ApplicantIntership Delete"})
  
    

#  Applicants  

class ApplicantsAPI(APIView):
    def get(self,request,id=None):
        obj_applicants = Applicants.objects.all()
        serializer = ApplicantsSerializer(obj_applicants,many=True)
        return Response(serializer.data)    
    

    # def post(self,request):
    #     data = request.data
    #     serializer = ApplicantsSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status":"200 successfully  Applicants ADDED"})
    #     return Response(serializer.errors)
    

    def post(self,request):
        jsondata = request.data
        user_data = {
            'username':jsondata['username'],
            'first_name':jsondata['first_name'],
            'last_name':jsondata['last_name'],
            'email':jsondata['email'],
        }

        applicant_data = {
            'gender':jsondata['gender'],
            'date_of_birth':jsondata['date_of_birth'],
            'phone_number':jsondata['phone_number'],
            'martial_status':jsondata['martial_status'],
            'home_town':jsondata['home_town'],
            'permanent_address':jsondata['permanent_address'],
            'pincode':jsondata['pincode'],
            'current_location':jsondata['current_location'],
            'resume':jsondata['resume'],
            'preferred_job_type':jsondata['preferred_job_type'],
            'preferred_job_type':jsondata['preferred_job_type'],
            'total_years_of_experience':jsondata['total_years_of_experience'],
            'availability_to_join':jsondata['availability_to_join'],
            'work_permit_for_USA':jsondata['work_permit_for_USA'],
            'langauages':jsondata['langauages'],
            'about':jsondata['about']
            }
        

        user_objs = User.objects.create(**user_data)
        user_objs.set_password(jsondata['password'])
        user_objs.save()


        applicant_objects = Applicants.objects.create(User_id=user_objs,**applicant_data)
        applicant_objects.save()

        serializer = ApplicantsSerializer(applicant_objects,data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"200 successfully  Applicants ADDED"})
        return Response(serializer.errors)
        

        


    def put(self,request,id):
        data = request.data
        appli = Applicants.objects.get(id=id)
        serializer = ApplicantsSerializer(appli,data=data)


        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Update applicant successfully"})
        return Response({"status":"Not Update applicant"})
    

    def delete(self,request,id):
        appli = Applicants.objects.get(id=id)
        appli.delete()
        return Response({"status":"Applicant Delete"})
    

    
    




