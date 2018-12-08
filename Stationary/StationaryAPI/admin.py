from django.contrib import admin
from .models import Item,CurrentItems,Dealer,Faculty,Vendor,OrderItems,Order,SupplyOrderItems,SupplyOrder
# Register your models here.
admin.site.register(Item)
admin.site.register(CurrentItems)
admin.site.register(Dealer)
admin.site.register(Faculty)
admin.site.register(Vendor)
admin.site.register(OrderItems)
admin.site.register(Order)
admin.site.register(SupplyOrderItems)
admin.site.register(SupplyOrder)
