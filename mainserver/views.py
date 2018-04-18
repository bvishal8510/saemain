from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import TokenAuthentication
from .models import User_main
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


class LoginViewSet(viewsets.ModelViewSet):
    
    queryset = User_main.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post',]

    def perform_create(self, serializer):
        print(serializer)
        email = serializer.data["email"]
        user = User.objects.get(email=email)
        t = Token.objects.create(user=user)
        serializer.save()
        return serializer.data
