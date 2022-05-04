from django.shortcuts import render
from food_order.models import *
from food_order.serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework import filters as searchfilter

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['email','password']

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class DeliveryManList(generics.ListCreateAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer

class DeliveryManDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer

class AdminUserList(generics.ListCreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

class AdminUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['categoryId', "name"]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price',lookup_expr='lte')
    class Meta:
        model = Item
        fields = [
            'isRawMaterial',
            'categoryId',
            'min_price',
            'max_price',
            ]

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by('-id')
    serializer_class = ItemSerializer
    filter_backends =[searchfilter.SearchFilter,DjangoFilterBackend]
    filterset_class = ItemFilter
    search_fields = ['name']

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all().order_by('-id')
    serializer_class = ItemSerializer

class ShoppingCartList(generics.ListCreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['clientId']

class ShoppingCartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class SalesOrderList(generics.ListCreateAPIView):
    queryset = SalesOrder.objects.order_by('-id')
    serializer_class = SalesOrderSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['clientId']

class SalesOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrder.objects.all().order_by('-id')
    serializer_class = SalesOrderSerializer
    

class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.order_by('-id')
    serializer_class = PurchaseOrderSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['supplierId']

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all().order_by('-id')
    serializer_class = PurchaseOrderSerializer

class NewOrderList(generics.ListCreateAPIView):
    queryset = NewOrder.objects.order_by('-id')
    serializer_class = NewOrderSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['supplierId']

class NewOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewOrder.objects.all().order_by('-id')
    serializer_class = NewOrderSerializer

class ShippingOrderList(generics.ListCreateAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = ShippingOrderSerializer
    filter_backends =[DjangoFilterBackend]

class ShippingOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrder.objects.all()
    serializer_class = ShippingOrderSerializer

class RawMaterialList(generics.ListCreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class RawMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class ShoppingCartItemList(generics.ListCreateAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['shoppingCartId']

class ShoppingCartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer

class SalesOrderItemList(generics.ListCreateAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['salesOrderId']

class SalesOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemSerializer

class PurchaseOrderItemList(generics.ListCreateAPIView):
    queryset = PurchaseOrdersItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['purchaseOrderId']

class PurchaseOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrdersItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

class NewOrderItemList(generics.ListCreateAPIView):
    queryset = NewOrdersItem.objects.all()
    serializer_class = NewOrderItemSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['newOrderId']

class NewOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewOrdersItem.objects.all()
    serializer_class = NewOrderItemSerializer

class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['clientId']

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['itemId']

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['deliveryManId']

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
