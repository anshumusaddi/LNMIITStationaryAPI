from django.shortcuts import render
from rest_framework import generics
from .models import Item,CurrentItems,Dealer,Faculty,Vendor,OrderItems,Order,SupplyOrderItems,SupplyOrder
from .serializers import ItemSerializer,FacultySerializer,CurrItSerializer,VendorSerializer,DealerSerializer,OrderSerializer,OrderItemsSerializer,SupplyOrderSerializer,SupplyOrderItemsSerializer,CurrItEditSerializer,DealerEditSerializer,OrderEditSerializer,OrderItemsEditSerializer
# Create your views here.
class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()

class ItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        serializer.save()

class CurrentItemsListView(generics.ListCreateAPIView):
    queryset = CurrentItems.objects.all()
    serializer_class = CurrItSerializer

    def perform_create(self, serializer):
        serializer.save()

class CurrentItemsInsertView(generics.ListCreateAPIView):
    queryset = CurrentItems.objects.all()
    serializer_class = CurrItEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class CurrentEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrentItems.objects.all()
    serializer_class = CurrItEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class CurrentFacultyIDView(generics.ListCreateAPIView):
    serializer_class = CurrItSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        return CurrentItems.objects.filter(fac__FID__iexact = facu)

    def perform_create(self, serializer):
        serializer.save()

class CurrentFacultyNameView(generics.ListCreateAPIView):
    serializer_class = CurrItSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        return CurrentItems.objects.filter(fac__Name__icontains = facu)

    def perform_create(self, serializer):
        serializer.save()

class CurrentItemIDView(generics.ListCreateAPIView):
    serializer_class = CurrItSerializer

    def get_queryset(self):

        itid = self.kwargs['itid']
        return CurrentItems.objects.filter(item__PID__iexact = itid)

    def perform_create(self, serializer):
        serializer.save()

class CurrentItemNameView(generics.ListCreateAPIView):
    serializer_class = CurrItSerializer

    def get_queryset(self):

        itn = self.kwargs['itn']
        return CurrentItems.objects.filter(item__Name__icontains = itn)

    def perform_create(self, serializer):
        serializer.save()

class FacultyListView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def perform_create(self, serializer):
        serializer.save()

class FacultyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

    def perform_create(self, serializer):
        serializer.save()

class VendorListView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_create(self, serializer):
        serializer.save()

class VendorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_create(self, serializer):
        serializer.save()

class DealerListView(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

    def perform_create(self, serializer):
        serializer.save()

class DealerInsertView(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class DealerEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class DealerVendorIDView(generics.ListCreateAPIView):
    serializer_class = DealerSerializer

    def get_queryset(self):

        vend = self.kwargs['vend']
        return Dealer.objects.filter(ven__VID__iexact = vend)

    def perform_create(self, serializer):
        serializer.save()

class DealerVendorNameView(generics.ListCreateAPIView):
    serializer_class = DealerSerializer

    def get_queryset(self):

        vend = self.kwargs['vend']
        return Dealer.objects.filter(ven__Name__icontains = vend)

    def perform_create(self, serializer):
        serializer.save()

class DealerItemIDView(generics.ListCreateAPIView):
    serializer_class = DealerSerializer

    def get_queryset(self):

        itm = self.kwargs['itm']
        return Dealer.objects.filter(item__PID__iexact = itm)

    def perform_create(self, serializer):
        serializer.save()

class DealerItemNameView(generics.ListCreateAPIView):
    serializer_class = DealerSerializer

    def get_queryset(self):

        itm = self.kwargs['itm']
        return Dealer.objects.filter(item__Name__icontains = itm)

    def perform_create(self, serializer):
        serializer.save()

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderInsertView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderFacultyIDView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        return Order.objects.filter(faculty__FID__iexact = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderFacultyNameView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        return Order.objects.filter(faculty__Name__icontains = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderApprovedView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        app = self.kwargs['app']
        if(app=="null"):
            return Order.objects.filter(Approved__isnull = True)
        elif(app=="True" or app=="true"):
            return Order.objects.filter(Approved = True)
        else:
            return Order.objects.filter(Approved = False)

    def perform_create(self, serializer):
        serializer.save()

class OrderDeliveredView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        deli = self.kwargs['deli']
        if(deli=="True" or deli=="true"):
            return Order.objects.filter(Delivered = True)
        else:
            return Order.objects.filter(Delivered = False)

    def perform_create(self, serializer):
        serializer.save()

class OrderApprovedDeliveredView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        app = self.kwargs['app']
        deli = self.kwargs['deli']
        if(app=="null" and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved__isnull = True,Delivered = True)
        elif(app=="null" and (deli=="False" or deli=="false")):
            return Order.objects.filter(Approved__isnull = True,Delivered = False)
        elif((app=="True" or app=="true") and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved = True,Delivered = True)
        elif((app=="True" or app=="true") and (deli=="False" or deli=="false")):
            return Order.objects.filter(Approved = True,Delivered = False)
        elif((app=="False" or app=="false") and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved = False,Delivered = True)
        else:
            return Order.objects.filter(Approved = False,Delivered = False)

    def perform_create(self, serializer):
        serializer.save()

class OrderFacultyIDApprovedView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        app = self.kwargs['app']
        if(app=="null"):
            return Order.objects.filter(Approved__isnull = True,faculty__FID__iexact = facu)
        elif(app=="True" or app=="true"):
            return Order.objects.filter(Approved = True,faculty__FID__iexact = facu)
        else:
            return Order.objects.filter(Approved = False,faculty__FID__iexact = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderFacultyIDDeliveredView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        deli = self.kwargs['deli']
        if(deli=="True" or deli=="true"):
            return Order.objects.filter(Delivered = True,faculty__FID__iexact = facu)
        else:
            return Order.objects.filter(Delivered = False,faculty__FID__iexact = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderFIDAppDelView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        app = self.kwargs['app']
        deli = self.kwargs['deli']
        if(app=="null" and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved__isnull = True,Delivered = True,faculty__FID__iexact = facu)
        elif(app=="null" and (deli=="False" or deli=="false")):
            return Order.objects.filter(Approved__isnull = True,Delivered = False,faculty__FID__iexact = facu)
        elif((app=="True" or app=="true") and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved = True,Delivered = True,faculty__FID__iexact = facu)
        elif((app=="True" or app=="true") and (deli=="False" or deli=="false")):
            return Order.objects.filter(Approved = True,Delivered = False,faculty__FID__iexact = facu)
        elif((app=="False" or app=="false") and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved = False,Delivered = True,faculty__FID__iexact = facu)
        else:
            return Order.objects.filter(Approved = False,Delivered = False,faculty__FID__iexact = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderFacultyNameApprovedView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        app = self.kwargs['app']
        if(app=="null"):
            return Order.objects.filter(Approved__isnull = True,faculty__Name__icontains = facu)
        elif(app=="True" or app=="true"):
            return Order.objects.filter(Approved = True,faculty__Name__icontains = facu)
        else:
            return Order.objects.filter(Approved = False,faculty__Name__icontains = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderFacultyNameDeliveredView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        deli = self.kwargs['deli']
        if(deli=="True" or deli=="true"):
            return Order.objects.filter(Delivered = True,faculty__Name__icontains = facu)
        else:
            return Order.objects.filter(Delivered = False,faculty__Name__icontains = facu)

    def perform_create(self, serializer):
        serializer.save()

class OrderFNameAppDelView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):

        facu = self.kwargs['facu']
        app = self.kwargs['app']
        deli = self.kwargs['deli']
        if(app=="null" and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved__isnull = True,Delivered = True,faculty__Name__icontains = facu)
        elif(app=="null" and (deli=="False" or deli=="false")):
            return Order.objects.filter(Approved__isnull = True,Delivered = False,faculty__Name__icontains = facu)
        elif((app=="True" or app=="true") and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved = True,Delivered = True,faculty__Name__icontains = facu)
        elif((app=="True" or app=="true") and (deli=="False" or deli=="false")):
            return Order.objects.filter(Approved = True,Delivered = False,faculty__Name__icontains = facu)
        elif((app=="False" or app=="false") and (deli=="True" or deli=="true")):
            return Order.objects.filter(Approved = False,Delivered = True,faculty__Name__icontains = facu)
        else:
            return Order.objects.filter(Approved = False,Delivered = False,faculty__Name__icontains = facu)

    def perform_create(self, serializer):
        serializer.save()


class OrderItemsListView(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderItemsOIDView(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

    def get_queryset(self):
        OID = self.kwargs['OID']
        return OrderItems.objects.filter(ord = OID)

    def perform_create(self, serializer):
        serializer.save()

class OrderItemsInsertView(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderItemsEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsEditSerializer

    def perform_create(self, serializer):
        serializer.save()

class SupplyOrderListView(generics.ListCreateAPIView):
    queryset = SupplyOrder.objects.all()
    serializer_class = SupplyOrderSerializer

    def perform_create(self, serializer):
        serializer.save()

class SupplyOrderItemsListView(generics.ListCreateAPIView):
    queryset = SupplyOrderItems.objects.all()
    serializer_class = SupplyOrderItemsSerializer

    def perform_create(self, serializer):
        serializer.save()
