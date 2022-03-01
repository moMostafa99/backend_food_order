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
    filterset_fields = ['email','password','provider']

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

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['categoryId']

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

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

class PurchaseOrderList(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['clientId']

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class ShippingOrderList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = ShippingOrderSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['deliveryManId']

class ShippingOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = ShippingOrderSerializer

class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

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

class PurchaseOrderItemList(generics.ListCreateAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

class PurchaseOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['clientId']

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class RateList(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class RateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer