from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    
from django.utils.decorators import method_decorator
from json import loads
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1+n2
        print(request_body)
        data={
            "sum":result
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name='dispatch')
class SubtractionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1-n2
        data={
            "Difference":result
        }
        return JsonResponse(data)        

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1*n2
        data={
            "multiplication":result
        }
        return JsonResponse(data)   


@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1/n2
        data={
            "Division":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ModulusView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n1=form_data.get("num1")
        n2=form_data.get("num2")
        result=n1%n2
        data={
            "Modulus":result
        }
        return JsonResponse(data)
        
        
@method_decorator(csrf_exempt,name='dispatch')
class BMI_View(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        weight=form_data.get("weight")
        height=form_data.get("height")
        height_in_meter=height/100
        bmi=weight/height_in_meter**2
        data={
            "weight":weight,
            "Height":height,
            "BMI":bmi,
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class Age_calculatorView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        birth_year=form_data.get("birth_year")
        current_year=form_data.get("current_year")
        age=current_year-birth_year
        data={
            "age":age
        }   
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        total_marks=form_data.get("total_marks")
        obtained_marks=form_data.get("obtained_marks")
        percentage=(obtained_marks/total_marks)*100
        data={
            "percentage":percentage
        }
        return JsonResponse(data)
