from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Myclass(APIView):
    def get(self,request):
        return Response({"message":"Good Morning"})

class AdditionView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")

        result=x+y
        return Response({"result":result})    

class SubtractionView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")

        result=x-y
        return Response({"result":result})

class MultiplicationView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2") 

        result=x*y
        return Response({"result":result})


class LargestView(APIView):
    def post(self,request):
        x=request.data.get("num1")
        y=request.data.get("num2")
        if x>y:
            return Response({"result":x})
        else:   
            return Response({"result":y})


class TempView(APIView):
    def post(self,request):
        celsius=request.data.get("temp")
        f=(celsius*9/5)+32
        return Response({"result":f})

    
