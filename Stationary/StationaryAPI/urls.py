"""Stationary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('item/',views.ItemListView.as_view(),name = 'Item List'),
    path('item/<pk>/',views.ItemView.as_view(),name = 'Item'),
    path('faculty/',views.FacultyListView.as_view(),name='Faculty List'),
    path('faculty/<pk>/',views.FacultyView.as_view(),name='Faculty'),
    path('vendor/',views.VendorListView.as_view(),name = 'Vendor List'),
    path('vendor/<pk>/',views.VendorView.as_view(),name = 'Vendor'),
    path('currentitems/',views.CurrentItemsListView.as_view(),name = 'Current Items'),
    path('currentitems/FID=<str:facu>/',views.CurrentFacultyIDView.as_view(),name = 'Current Item Faculty ID'),
    path('currentitems/FName=<str:facu>/',views.CurrentFacultyNameView.as_view(),name = 'Current Item Faculty Name'),
    path('currentitems/PID=<str:itid>/',views.CurrentItemIDView.as_view(),name = 'Current Item Item ID'),
    path('currentitems/IName=<str:itn>/',views.CurrentItemNameView.as_view(),name = 'Current Item Item Name'),
    path('currentitems/Insert/',views.CurrentItemsInsertView.as_view(),name = 'Current Items Insert'),
    path('currentitems/<pk>/',views.CurrentEditView.as_view(),name = 'Current Item Edit'),
    path('dealer/',views.DealerListView.as_view(),name = 'Dealer'),
    path('dealer/VID=<str:vend>/',views.DealerVendorIDView.as_view(),name = 'Dealer Vendor ID'),
    path('dealer/VName=<str:vend>/',views.DealerVendorNameView.as_view(),name = 'Dealer Vendor Name'),
    path('dealer/PID=<str:itm>/',views.DealerItemIDView.as_view(),name = 'Dealer Item ID'),
    path('dealer/IName=<str:itm>/',views.DealerItemNameView.as_view(),name = 'Dealer Item Name'),
    path('dealer/Insert/',views.DealerInsertView.as_view(),name = 'Dealer Insert'),
    path('dealer/<pk>/',views.DealerEditView.as_view(),name = 'Dealer Edit'),
    path('order/',views.OrderListView.as_view(),name = 'Order'),
    path('order/FID=<str:facu>/',views.OrderFacultyIDView.as_view(),name = 'Order Faculty ID'),
    path('order/FName=<str:facu>/',views.OrderFacultyNameView.as_view(),name = 'Order Faculty Name'),
    path('order/Approved=<str:app>/',views.OrderApprovedView.as_view(),name = 'Order Approved'),
    path('order/Delivered=<str:deli>/',views.OrderDeliveredView.as_view(),name = 'Order Delivered'),
    path('order/Approved=<str:app>/Delivered=<str:deli>/',views.OrderApprovedDeliveredView.as_view(),name = 'Order Approved Delivered'),
    path('order/Delivered=<str:deli>/Approved=<str:app>/',views.OrderApprovedDeliveredView.as_view(),name = 'Order Approved Delivered'),
    path('order/FID=<str:facu>/Approved=<str:app>/',views.OrderFacultyIDApprovedView.as_view(),name = 'Order Faculty ID Approved'),
    path('order/FID=<str:facu>/Delivered=<str:deli>/',views.OrderFacultyIDDeliveredView.as_view(),name = 'Order Faculty ID Delivered'),
    path('order/FID=<str:facu>/Approved=<str:app>/Delivered=<str:deli>/',views.OrderFIDAppDelView.as_view(),name = 'Order Faculty ID Approved Delivered'),
    path('order/FID=<str:facu>/Delivered=<str:deli>/Approved=<str:app>/',views.OrderFIDAppDelView.as_view(),name = 'Order Faculty ID Approved Delivered'),
    path('order/FName=<str:facu>/Approved=<str:app>/',views.OrderFacultyNameApprovedView.as_view(),name = 'Order Faculty Name Approved'),
    path('order/FName=<str:facu>/Delivered=<str:deli>/',views.OrderFacultyNameDeliveredView.as_view(),name = 'Order Faculty Name Delivered'),
    path('order/FName=<str:facu>/Approved=<str:app>/Delivered=<str:deli>/',views.OrderFNameAppDelView.as_view(),name = 'Order Faculty Name Approved Delivered'),
    path('order/FName=<str:facu>/Delivered=<str:deli>/Approved=<str:app>/',views.OrderFNameAppDelView.as_view(),name = 'Order Faculty Name Approved Delivered'),
    path('order/Insert/',views.OrderInsertView.as_view(),name = 'Order Insert'),
    path('order/<pk>/',views.OrderEditView.as_view(),name = 'Order Edit'),
    path('orderitems/',views.OrderItemsListView.as_view(),name = 'Order Items'),
    path('orderitems/OID=<int:OID>/',views.OrderItemsOIDView.as_view(),name = 'Order Items Single'),
    path('orderitems/Insert/',views.OrderItemsInsertView.as_view(),name = 'Order Items Insert'),
    path('orderitems/<pk>/',views.OrderItemsEditView.as_view(),name = 'Order Items Edit'),
    # Complete Above This
    path('supplyorder/',views.SupplyOrderListView.as_view(),name = 'Supply Order'),
    path('supplyorderitems/',views.SupplyOrderItemsListView.as_view(),name = 'Supply Order Items'),
]
