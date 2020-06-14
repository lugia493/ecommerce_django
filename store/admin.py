from django.contrib import admin

# Register your models here. In order to see models in http://localhost:8000/admin/

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
