from django.contrib import admin
from .models import City, DeliveryMan, Package
# Register your models here.

admin.site.register(City)
admin.site.register(DeliveryMan)
admin.site.register(Package)
