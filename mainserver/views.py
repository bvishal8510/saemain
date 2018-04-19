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


class LoginViewSet(APIView):

    def get(self, request):
        print(request)
        print(list(request))
        # user = User_main.objects.get(username = serializer.data['username'], email = serializer.data['email'], password = serializer.data['password'])
        print(1)
        # print(serializer.data)
        print(2)
        # print(user)
        # t = Token.objects.create(user = user)
        # print(t)
        # return user
        # return serializer.data
