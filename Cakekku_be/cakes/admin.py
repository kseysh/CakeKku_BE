from django.contrib import admin
from .models import *

admin.site.register(Cake)
admin.site.register(MyCake)
admin.site.register(OrderDetail)
admin.site.register(AdditionalOption)
admin.site.register(OrderDetailByMyCake)