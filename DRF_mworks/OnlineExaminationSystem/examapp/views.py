from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from examapp.models import QuestionDb
from examapp.serializers import QuestionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all()
        serializers_instance=QuestionSerializer(qs,many=True)
        return Response(data=serializers_instance.data)
    
    def post(self,request):  
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data
            QuestionDb.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
         
