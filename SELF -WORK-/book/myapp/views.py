from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import BookDB
from myapp.serializers import BookDbserializer

# Create your views here.
class BookListCreateView(APIView):
    def get(self,request):
        qs=BookDb.objects.all()
        serializer_instance=BookDbserializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=BookDbserializer(data=form_data)
        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data 

            BookDb.objects.create(**original_data)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
            
