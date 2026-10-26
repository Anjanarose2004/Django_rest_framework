from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionsDb
from Repository.serializers import QuestionDbserializer  
from Repository.models import SubmissionDb
from Repository.serializers import SubmissionSerializer

# Create your views here.
class QuestionsListCreateView(APIView):
    def get(self,request):
        #Retrive all questions from the QuestionDb model
        qs=QuestionsDb.objects.all()
        serializer_instance=QuestionDbserializer(qs,many=True) #serializer the queryset
        return Response(data=serializer_instance.data) #return the serialized data as a response


    def post(self,request):
        form_data=request.data #get the form data from the request
        #create a new question instance using the from data

        serializer_instance=QuestionDbserializer(data=form_data) #serializer the form data
        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data 
 
            QuestionsDb.objects.create(**original_data)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
            
        #QuestionsDb.objects.create(**form_data)
        #return Response(data={"message":"Question created successfully"})     

    
class QuestionsRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=QuestionsDb.objects.get(id=pk)
        serializer_instance=QuestionDbserializer(qs)
        return Response(data=serializer_instance.data) 

    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionDbserializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionsDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        QuestionsDb.objects.filter(id=pk).delete()

        return Response(
            {"Message":"Question deleted successfully"}
        )    


class SubmissionListCreateView(APIView):
    def get(self,request):
        qs=SubmissionDb.objects.all()
        serializer_instance=SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data
            SubmissionDb.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

        from django.shortcuts import render,get_object_or_404
 

class submissionRetrieveUpdateDelete(APIView):

    def get(self,request,pk):
        # qs=SubmissionsDb.objects.get(id=pk)
        qs=get_object_or_404(SubmissionDb,id=pk) #Retrieves an object by primary key; returns a 404 error if not found.
        serializer_instance=SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual=serializer_instance.validated_data
            SubmissionDb.objects.filter(id=pk).update(**actual)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
class EvaluateSubmissionView(APIView):
    def put(self,request,pk):
        form_data=request.data
        SubmissionDb.objects.filter(id=pk).update(**form_data)
        return Response(data={
            "Message":"Updated...!"
        })