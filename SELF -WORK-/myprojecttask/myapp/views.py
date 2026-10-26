from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import MyModel 

# Create your views here.
class MyModelView(APIView):
    def get(self, request):
        qs=MyModel.objects.all().values()
        result=list(qs)
        return Response(result)
     