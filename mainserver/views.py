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
from mainsae.settings import EMAIL_HOST_USER
import requests
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail


class LoginViewSet(viewsets.ViewSet):

    def list(self, request):
        d1 = {}
        try:
            user = User.objects.get(email= request.GET['email'], username = request.GET['username'],
             password = request.GET['password'] )
            user1 = User_main.objects.get(email= request.GET['email'], username = request.GET['username'],
             password = request.GET['password'] )
        except User.DoesNotExist:
            user = None
        if user:
            d1['user'] = 1
            d1['customer_id'] = user1.Customer_id
            t = Token.objects.create(user = user)
            # t = 1
        else:
            t = 0
            d1['user'] = 0
        d1['token'] = str(t)
        return Response(d1)


class Get_Bal(APIView):
    
    def get(self, request, format=None):
        d = {}
        user = User_main.objects.get(email = dict(request.GET)['email'][0])
        d['balance'] = user.energy_bal
        return Response(d)

    def put(self, request):
        print(request.data)
        user = User_main.objects.filter(email = dict(request.data)['email'][0]).update(energy_bal = dict(request.data)['energy'][0])
        print(user)
        return HttpResponse("done")


class Forget_password(APIView):

    def get(self, request):
        email = dict(request.GET)["email"][0]
        user = User.objects.get(email = email)
        d = {}
        if user:
            d['user'] = '1'
            message = 'Dear customer, this is your password for the account is ' + str(user.password)
            subject = 'Recieve Password'
            from_mail = EMAIL_HOST_USER
            to_mail = [email]
            send_mail(subject,
                            message,
                            from_mail,
                            to_mail,
                            fail_silently=False
                            )
            return Response(d)
        d['user'] = '0'
        return Response(d)

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
