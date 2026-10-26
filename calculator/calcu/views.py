from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


@method_decorator(csrf_exempt, name='dispatch')
class SquareView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        num = form_data.get("num")

        result = num * num

        data = {
            "square": result
        }

        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class CubeView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        num = form_data.get("num")

        result = num * num * num

        data = {
            "cube": result
        }

        return JsonResponse(data)