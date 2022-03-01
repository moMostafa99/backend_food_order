from rest_framework import serializers
from food_order.models import *
from django.db.models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'comment',
            'createdDate',
            'clientId',
            'itemId',
        ]

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = [
            'id',
            'rate',
            'createdDate',
            'clientId',
            'itemId',
        ]

class FavoriteSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = Favorite
        fields = [
            'id',
            'clientId',
            'itemId',
            'item'
        ]
    def get_item(self, instance):
        item = Item.objects.get(id=str(instance.itemId.id))
        return ItemSerializer(item).data 

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = PurchaseOrderItem
        fields = [
            'id',
            'quantity',
            'itemId',
            'purchaseOrderId',
            'item'
        ]
    def get_item(self, instance):
        item = Item.objects.get(id=str(instance.itemId.id))
        return ItemSerializer(item).data

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    item_shoppingcartitem = serializers.SerializerMethodField()
    class Meta:
        model = ShoppingCartItem
        fields = [
            'id',
            'quantity',
            'itemId',
            'shoppingCartId',
            'item_shoppingcartitem'
        ]
    def get_item_shoppingcartitem(self, instance):
        item = Item.objects.get(id=str(instance.itemId.id))
        return ItemSerializer(item).data

class RawMaterialItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
                'id',
                'name',
                'price',
                'amount',
                'isRawMaterial',
                'description',
                'categoryId',
            ]

class RawMaterialSerializer(serializers.ModelSerializer):
    rawmaterialitem_rawmaterial = serializers.SerializerMethodField()
    class Meta:
        model = RawMaterial
        fields = [
            'id',
            'itemId',
            'rawMaterialItemId',
            'rawmaterialitem_rawmaterial'
        ]
    def get_rawmaterialitem_rawmaterial(self, instance):
        item = Item.objects.get(id=str(instance.rawMaterialItemId.id))
        return RawMaterialItemSerializer(item).data

class TrackSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Track
        fields = [
            'id',
            'createdDate',
            'deliveryId',
            'statusId',
            'status',
        ]
    def get_status(self, instance):
        status = Status.objects.get(id=str(instance.statusId.id))
        return StatusSerializer(status).data

class PurchaseOrderBaiscSerializer(serializers.ModelSerializer):
    purchaseorder_purchaseorderitem = PurchaseOrderItemSerializer(read_only=True,many=True)
    class Meta:
        model = PurchaseOrder
        fields = [
            'id',
            'paymentMethod',
            'createdDate',
            'clientId',
            'supplierId',
            'purchaseorder_purchaseorderitem',
        ]

class ShippingOrderSerializer(serializers.ModelSerializer):
    delivery_track = TrackSerializer(read_only=True,many=True)
    deliveryMan = serializers.SerializerMethodField()
    purchaseOrder = serializers.SerializerMethodField()
    class Meta:
        model = Delivery
        fields = [
            'district',
            'streetName',
            'building',
            'floor',
            'apartment',
            'createdDate',
            'purchaseOrderId',
            'purchaseOrder',
            'deliveryManId',
            'deliveryMan',
            'delivery_track'
        ]
    def get_deliveryMan(self, instance):
        deliveryMan = DeliveryMan.objects.get(userId=str(instance.deliveryManId.userId.id))
        return DeliveryManSerializer(deliveryMan).data
    def get_purchaseOrder(self, instance):
        purchaseOrder = PurchaseOrder.objects.get(id=str(instance.purchaseOrderId.id))
        return PurchaseOrderBaiscSerializer(purchaseOrder).data

class DeliverySerializer(serializers.ModelSerializer):
    delivery_track = TrackSerializer(read_only=True,many=True)
    deliveryMan = serializers.SerializerMethodField()
    class Meta:
        model = Delivery
        fields = [
            'district',
            'streetName',
            'building',
            'floor',
            'apartment',
            'createdDate',
            'purchaseOrderId',
            'deliveryManId',
            'deliveryMan',
            'delivery_track'
        ]
    def get_deliveryMan(self, instance):
        deliveryMan = DeliveryMan.objects.get(userId=str(instance.deliveryManId.userId.id))
        return DeliveryManSerializer(deliveryMan).data

class PurchaseOrderSerializer(serializers.ModelSerializer):
    purchaseorder_delivery = DeliverySerializer(read_only=True,many=False)
    purchaseorder_purchaseorderitem = PurchaseOrderItemSerializer(read_only=True,many=True)
    class Meta:
        model = PurchaseOrder
        fields = [
            'id',
            'paymentMethod',
            'createdDate',
            'clientId',
            'supplierId',
            'purchaseorder_purchaseorderitem',
            'purchaseorder_delivery',
        ]

class ShoppingCartSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()
    class Meta:
        model = ShoppingCart
        fields = [
            'clientId',
            'client'
        ]
    def get_client(self, instance):
        client = Client.objects.get(userId=str(instance.clientId.userId.id))
        return ClientSerializer(client).data

class ItemSerializer(serializers.ModelSerializer):
    item_rawmaterial = RawMaterialSerializer(many=True,read_only=True)
    category = serializers.SerializerMethodField()
    rateList = serializers.SerializerMethodField()
    reviewList = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'price',
            'image',
            'amount',
            'isRawMaterial',
            'description',
            'categoryId',
            'category',
            'rateList',
            'reviewList',
            'item_rawmaterial'
        ]
    def get_category(self, instance):
        category = Category.objects.get(id=str(instance.categoryId.id))
        return CategoryBasicSerializer(category).data
    
    def get_rateList(self, instance):
        rateList = Rate.objects.filter(itemId=str(instance.id))
        return RateSerializer(rateList,many=True).data
    
    def get_reviewList(self, instance):
        reviewList = Review.objects.filter(itemId=str(instance.id))
        return ReviewSerializer(reviewList,many=True).data

class CategoryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'categoryId',
        ]
    
class CategorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    category_subcategory = CategoryBasicSerializer(read_only=True,many=True)
    category_item = ItemSerializer(read_only=True,many=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'categoryId',
            'category',
            'category_subcategory',
            'category_item'
        ]
    def get_category(self, instance):
        if(instance.categoryId is not None):
            category = Category.objects.get(id=str(instance.categoryId.id))
            return CategoryBasicSerializer(category).data

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'name',
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'phone',
            'email',
            'password',
            'userType',
            'provider'
        ]

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = [
            'userId',
            'user'
        ]
    def get_user(self, instance):
        user = User.objects.get(id=str(instance.userId.id))
        return UserSerializer(user).data

class DeliveryManSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = DeliveryMan
        fields = [
            'userId',
            'user'
        ]
    def get_user(self, instance):
        user = User.objects.get(id=str(instance.userId.id))
        return UserSerializer(user).data

class SupplierSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Supplier
        fields = [
            'userId',
            'user'
        ]
    def get_user(self, instance):
        user = User.objects.get(id=str(instance.userId.id))
        return UserSerializer(user).data

