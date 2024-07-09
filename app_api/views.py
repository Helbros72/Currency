from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
def test_api(request):
    return HttpResponse("Hello World")


class T_Api(APIView):
    def get(self, request):
        return Response({"Method": "GET"})


class P_Api(APIView):
    def post(self, request):

        text = request.data.get('text')
        print(text)
        return Response(text, status=status.HTTP_201_CREATED)
