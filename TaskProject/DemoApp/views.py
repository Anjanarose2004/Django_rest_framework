from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads 

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class FactorialView(View):
    def post(self,request):
        request_body=request.body
        form_data=loads(request_body)
        n =form_data.get("numbers")
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        data={
            "factorial":fact
        }    
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')    
class SimpleInterestView(View):
    def post(self,request):
        request_body=request.body
        data=loads(request_body)
        p=data.get("principle")
        r=data.get("rate")
        t=data.get("time")
        SI=(p*r*t)/100
        data={
            "principle":p,
            "rate":t,
            "time":r,
            "s":SI
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')        
class DiscountView(View):
    def post(self,request):
        request_body=request.body  
        data=loads(request_body)    
        p=data.get("Price")
        dp=data.get("Discount_percentage")
        dm=data.get("Disount_amount")
        fp=data.get("Final_price")
        discount=p*dp/100 
        final=p-discount
        data={
            "price":p,
            "discount":dp,
            "discount_amount":discount,
            "final_price":final
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        request_body=request.body
        data=loads(request_body)
        c=data.get("cost_price")
        sp=data.get("selling_price")
        profit=sp-c
        data={
            "cost_price":c,
            "selling_price":sp,
            "profit":profit
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        request_body=request.body
        data=loads(request_body)
        bs=data.get("basic_salary")
        b=data.get("bonus")
        d=data.get("deduction")
        result=bs+b-d
        data={
            "basic_salary":bs,
            "bonus":b,
            "deduction":d,
            "net_salary":result
        }
        return JsonResponse(data)