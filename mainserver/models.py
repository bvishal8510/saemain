from django.db import models


class User_main(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=70,blank=False)
    Token = models.CharField(max_length=200,blank=False)
    meter_no = models.IntegerField(blank = False)

class Meter_main(models.Model):
    meter_no = models.ForeignKey(User_main, on_delete=models.CASCADE)
    email = models.ForeignKey(User_main, on_delete=models.CASCADE)
    on_off = models.BooleanField(default = False)
    energy_bal = models.FloatField(blank=False)
    
class Payment_main(models.Model):
    email = models.ForeignKey(User_main, on_delete=models.CASCADE)
    amount = models.IntegerField(blank = False)
    order_id = models.CharField(max_length=200, blank = False)
    date = models.DateField(auto_now_add=True)

# class Meter_details(models.Model):
#     meter_no = models.IntegerField(blank=False)
#     elec_remain = models.IntegerField(blank=False, default = 0)