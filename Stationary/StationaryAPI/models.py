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
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    FID = models.CharField(max_length=100,primary_key=True)
    CurrIt = models.ManyToManyField(Item,through = 'CurrentItems',through_fields=('faculty', 'item'))

class Vendor(models.Model):
    VID = models.CharField(max_length=100,primary_key=True)
    Name = models.CharField(max_length = 100)
    DealsIn = models.ManyToManyField(Item,through = 'Dealer',through_fields=('vendor', 'item'))

class Dealer(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    price = models.FloatField()

class CurrentItems(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()
