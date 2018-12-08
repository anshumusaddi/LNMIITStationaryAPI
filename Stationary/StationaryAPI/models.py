from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    PID = models.BigAutoField(primary_key=True)
    Perishable = models.BooleanField(null=False,default=False)
    Name = models.CharField(max_length = 100)
    OnHold = models.PositiveIntegerField()
    MinQty = models.PositiveIntegerField()
    Qty = models.PositiveIntegerField()

class Faculty(models.Model):
    FID = models.CharField(max_length=100,primary_key=True)
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    CurrIt = models.ManyToManyField(Item,related_name='curritems',through = 'CurrentItems',through_fields=('faculty', 'item'))

class Vendor(models.Model):
    VID = models.CharField(max_length=100,primary_key=True)
    Name = models.CharField(max_length = 100)
    DealsIn = models.ManyToManyField(Item,related_name='deal',through = 'Dealer',through_fields=('vendor', 'item'))

class Dealer(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    price = models.FloatField()

class CurrentItems(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()

class Order(models.Model):
    OrderID = models.BigAutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty,related_name='fact',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,related_name='orditems',through = 'OrderItems',through_fields=('oid', 'item'))
    Approved = models.BooleanField(null=True)
    Delivered = models.BooleanField(null=False,default=False)
    OrderDate = models.DateField(auto_now_add=True)
    DeliveryDate = models.DateField()

class OrderItems(models.Model):
    oid = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()

class SupplyOrder(models.Model):
    OrderID = models.BigAutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor,related_name='vend',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,related_name='supplyorditems',through = 'SupplyOrderItems',through_fields=('oid', 'item'))
    OrderDate = models.DateField(auto_now_add=True)
    DeliveryDate = models.DateField()
    Paid = models.BooleanField(null=False,default=False)
    Delivered = models.BooleanField(null=False,default=False)

class SupplyOrderItems(models.Model):
    oid = models.ForeignKey(SupplyOrder,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()
