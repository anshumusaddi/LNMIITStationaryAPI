from rest_framework import serializers
from .models import Item,CurrentItems,Dealer,Faculty,Vendor,OrderItems,Order,SupplyOrderItems,SupplyOrder

class ItemSerializer(serializer.ModelSerializer):
    class Meta:
        model = Item
        fields = ("PID","Name","Perishable","Qty","OnHold","MinQty","OrderReq")

class FacultySerializerWOI(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ("FID", "Name","Email")

class CurrItSerializer(serializer.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = CurrIt
        fields = ("item","Qty")

class FacultySerializerWI(serializers.ModelSerializer):
    user = UserSerializer()
    CurrIt = CurrItSerializer(many=True)
    class Meta:
        model = Faculty
        fields = ("FID", "Name","Email","CurrIt")

class VendorSerializerWOI(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ("VID","name")

class DealerSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = Dealer
        fields = ("item","price")

class VendorSerializerWI(serializers.ModelSerializer):
    DealsIn = DealerSerializer(many=True)
    class Meta:
        model = Vendor
        fields = ("VID","name","DealsIn")

class OrderItemsSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = OrderItems
        fields = ("item","Qty")

class OrderSerializer(serializers.ModelSerializer):
    faculty = facultySerializerWOI()
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ("OrderID","faculty","items","Approved","Delivered","OrderDate","DeliveryDate")

class SupplyOrderItemsSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        model = SupplyOrderItems
        fields = ("item","Qty")

class SupplyOrderSerializer(serializers.ModelSerializer):
    vendor = VendorSerializerWOI()
    items = SupplyOrderItemsSerializer(many=True)
    class Meta:
        model = SupplyOrder
        ields = ("OrderID","vendor","items","Paid","Delivered","OrderDate","DeliveryDate")
