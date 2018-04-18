from django.db import models


class User_main(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=70,blank=False)
    password = models.CharField(max_length=250)
    Token = models.CharField(max_length=200)
    meter_no = models.IntegerField(blank = False)

class Meter_main(models.Model):
    name = models.ForeignKey(User_main, on_delete=models.CASCADE)
    on_off = models.BooleanField(default = False)
    energy_bal = models.FloatField(blank=False)
    
class Payment_main(models.Model):
    email = models.ForeignKey(User_main, on_delete=models.CASCADE)
    amount = models.IntegerField(blank = False)
    order_id = models.CharField(max_length=200, blank = False)
    date = models.DateField(auto_now_add=True)

class Rate(models.Model):
    rate = models.IntegerField()