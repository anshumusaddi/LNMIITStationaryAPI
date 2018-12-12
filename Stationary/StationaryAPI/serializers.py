from rest_framework import serializers
from .models import Item,CurrentItems,Dealer,Faculty,Vendor,OrderItems,Order,SupplyOrderItems,SupplyOrder

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("PID","Name","Perishable","Qty","OnHold","MinQty","OrderReq")

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ("FID", "Name","Email")

class CurrItSerializer(serializers.ModelSerializer):
    fac = FacultySerializer()
    item = ItemSerializer()
    class Meta:
        model = CurrentItems
        fields = ("id","fac","item","Qty")

class CurrItEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentItems
        fields = ("id","fac","item","Qty")

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ("VID","Email","Name")

class DealerSerializer(serializers.ModelSerializer):
    ven = VendorSerializer()
    item = ItemSerializer()
    class Meta:
        model = Dealer
        fields = ("id","ven","item","price")

class DealerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ("id","ven","item","price")

class OrderSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()
    class Meta:
        model = Order
        fields = ("OrderID","faculty","items","Approved","Delivered","OrderDate","DeliveryDate")

class OrderEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("OrderID","faculty","items","Approved","Delivered","OrderDate","DeliveryDate")

class OrderItemsSerializer(serializers.ModelSerializer):
    ord = OrderSerializer()
    item = ItemSerializer()
    class Meta:
        model = OrderItems
        fields = ("id","ord","item","Qty")

class OrderItemsEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ("id","ord","item","Qty")

class SupplyOrderSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    class Meta:
        model = SupplyOrder
        fields = ("OrderID","vendor","items","Paid","Delivered","OrderDate","DeliveryDate")

class SupplyOrderItemsSerializer(serializers.ModelSerializer):
    sord = SupplyOrderSerializer()
    item = ItemSerializer()
    class Meta:
        model = SupplyOrderItems
        fields = ("sord","item","Qty")
