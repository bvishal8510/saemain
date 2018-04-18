from django.contrib import admin
from mainserver.models import User_main, Payment_main, Meter_main, Rate

admin.site.register(User_main)
admin.site.register(Payment_main)
admin.site.register(Meter_main)
admin.site.register(Rate)