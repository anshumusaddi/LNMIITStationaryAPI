from django.db import models

# Create your models here.
class Item(models.Model):
    PID = models.BigAutoField(primary_key=True)
    Perishable = models.BooleanField(null=False,default=False)
    Name = models.CharField(max_length = 100)
    OnHold = models.PositiveIntegerField()
    MinQty = models.PositiveIntegerField()
    Qty = models.PositiveIntegerField()
    OrderReq = models.BooleanField(null=False,default=False)
    def __str__(self):
        return str(self.PID) + ' : ' + str(self.Name)

class Faculty(models.Model):
    FID = models.CharField(max_length=100,primary_key=True)
    Name = models.CharField(max_length = 100)
    Email = models.EmailField()
    CurrIt = models.ManyToManyField(Item,through = "CurrentItems",through_fields = ('fac','item'),related_name='curritems')
    def __str__(self):
        return str(self.FID) + ' : ' + str(self.Name)

class CurrentItems(models.Model):
    fac = models.ForeignKey(Faculty,related_name='facn',on_delete=models.CASCADE)
    item = models.ForeignKey(Item,related_name='itemn',on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()
    # only non-perishable items should be there + last odered items if possible
    def __str__(self):
        return str(self.fac) + ' : ' + str(self.item)

    class Meta:
        unique_together = ('fac', 'item',)

class Vendor(models.Model):
    VID = models.CharField(max_length=100,primary_key=True)
    Name = models.CharField(max_length = 100)
    Email = models.EmailField()
    DealsIn = models.ManyToManyField(Item,through = 'Dealer',through_fields = ('ven','item'),related_name='deal')
    def __str__(self):
        return str(self.VID) + ' : ' + str(self.Name)

class Dealer(models.Model):
    ven = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return str(self.ven) + ' : ' + str(self.item)

    class Meta:
        unique_together = ('ven', 'item',)

class Order(models.Model):
    OrderID = models.BigAutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty,related_name='fact',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,through = 'OrderItems',through_fields = ('ord','item'),related_name='orditems')
    Approved = models.BooleanField(null=True)
    Delivered = models.BooleanField(null=False,default=False)
    OrderDate = models.DateField(auto_now_add=True)
    DeliveryDate = models.DateField(null = True,blank = True)
    def __str__(self):
        return str(self.OrderDate) + " : " +str(self.OrderID) + ' : ' + str(self.faculty)

class OrderItems(models.Model):
    ord = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()
    def __str__(self):
        return str(self.ord) + " : " + str(self.item)

    class Meta:
        unique_together = ('ord', 'item',)

class SupplyOrder(models.Model):
    OrderID = models.BigAutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor,related_name='vend',on_delete=models.CASCADE)
    items = models.ManyToManyField(Item,through = 'SupplyOrderItems',through_fields = ('sord','item'),related_name='supplyorditems')
    OrderDate = models.DateField(auto_now_add=True)
    DeliveryDate = models.DateField(null=True,blank=True)
    Paid = models.BooleanField(null=False,default=False)
    Delivered = models.BooleanField(null=False,default=False)
    def __str__(self):
        return str(self.OrderDate) + " : " + str(self.OrderID) + ' : ' + str(self.vendor) #+ " : " self.items

class SupplyOrderItems(models.Model):
    sord = models.ForeignKey(SupplyOrder,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField()
    def __str__(self):
        return str(self.sord) + " : " + str(self.item)

    class Meta:
        unique_together = ('sord', 'item',)
