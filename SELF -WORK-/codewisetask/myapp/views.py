from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import QuestionsDb  

# Create your views here.
class QuestionsListCreateView(APIView):
    def get(self,request):
        qs=QuestionsDb.objects.all().values()
        result=list(qs)
        return Response(data=result)


    def post(self,request):
        form_data=request.data #get the form data from the request

        #create a new question instance using the from data

        QuestionsDb.objects.create(**form_data)

        return Response(data={"message":"Question created successfully"})      