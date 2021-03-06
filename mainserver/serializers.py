from rest_framework import serializers
from .models import User_main
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_main
        # model = User
        fields = ('username', 'email', 'password', 'address', 'meter_no')


# class PaymentSerializer(serializers.Serializer):
#     customer_id = serializers.CharField(max_length=100)
#     payment_amount = serializers.IntegerField()

#     class Meta:
#         fields = ('customer_id', 'payment_amount',)