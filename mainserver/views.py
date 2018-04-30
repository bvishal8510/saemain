from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import TokenAuthentication
from .models import User_main
from django.contrib.auth.models import User
from .serializers import UserSerializer
# from paytm.payments import PaytmPaymentPage
# from paytm import Checksum
from rest_framework.views import APIView
from django.http import HttpResponse
# from paytm.payments import VerifyPaytmResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, serializers
import json
import requests
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


class LoginViewSet(viewsets.ViewSet):

    def list(self, request):
        d1 = {}
        try:
            user = User.objects.get(email= request.GET['email'], username = request.GET['username'],
             password = request.GET['password'] )
        except User.DoesNotExist:
            user = None
        if user:
            d1['user'] = 1
            t = Token.objects.create(user = user)
        else:
            t = 0
            d1['user'] = 0
        d1['token'] = str(t)
        return Response(d1)

class BalViewSet(viewsets.ViewSet):

    def list(self, request):
        print(request.GET['user'])
        print(request.GET['user'].username)
        try:
            user = User.objects.get(email= request.GET['email'], username = request.GET['username'],
             password = request.GET['password'] )
        except User.DoesNotExist:
            user = None
        if user:
            t = Token.objects.create(user = user)
        else:
            t = 0
        d1 = {}
        d1['token'] = str(t)
        return Response(d1)

class Forget_password(APIView):

    def get(self, request):
        print(request.data)
        print(request.GET)
        # user = User.objects.get(email = request.GET)
        # print(user.password)
        return HttpResponse("enail sent")

    # def post(self, serializer):
    #     print(serializer)
    #     # print(list(request))
    #     # user = User_main.objects.get(username = serializer.data['username'], email = serializer.data['email'], password = serializer.data['password'])
    #     print(1)
    #     # print(serializer.data)
    #     # print(2)
    #     # print(user)
    #     # t = Token.objects.create(user = user)
    #     # print(t)
    #     # return user
    #     # return serializer.data
    #     return HttpResponse("dfgsdgf")
