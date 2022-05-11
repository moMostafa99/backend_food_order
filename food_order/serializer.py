from rest_framework import serializers
from food_order.models import *
from django.db.models import *

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


class SalesOrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = SalesOrderItem
        fields = [
            'id',
            'quantity',
            'itemId',
            'salesOrderId',
            'item'
        ]
    def get_item(self, instance):
        item = Item.objects.get(id=str(instance.itemId.id))
        return ItemSerializer(item).data

class NewOrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = NewOrdersItem
        fields = [
            'id',
            'quantity',
            'itemId',
            'newOrderId',
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

# class TrackSerializer(serializers.ModelSerializer):
#     status = serializers.SerializerMethodField()
#     class Meta:
#         model = Track
#         fields = [
#             'id',
#             'createdDate',
#             'deliveryId',
#             'statusId',
#             'status',
#         ]
#     def get_status(self, instance):
#         status = Status.objects.get(id=str(instance.statusId.id))
#         return StatusSerializer(status).data

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

class AdminUserSerializer(serializers.ModelSerializer):
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

class SalesOrderBaiscSerializer(serializers.ModelSerializer):
    salesorder_salesorderitem = SalesOrderItemSerializer(read_only=True,many=True)
    class Meta:
        model = SalesOrder
        fields = [
            'id',
            'paymentMethod',
            'createdDate',
            'clientId',
            'user',
            'salesorder_salesorderitem',
            'status',
            'rate',
            'address',
            'phone',
            'cost'
        ]


class ShippingOrderSerializer(serializers.ModelSerializer):
    deliveryMan = serializers.SerializerMethodField()
    class Meta:
        model = SalesOrder
        fields = [
            'address',
            'createdDate',
            'salesOrderId',
            'salesOrder',
            'deliveryManId',
            'deliveryMan',
            'status'
        ]
    def get_deliveryMan(self, instance):
        deliveryMan = DeliveryMan.objects.get(userId=str(instance.deliveryManId.userId.id))
        return DeliveryManSerializer(deliveryMan).data
    def get_salesOrder(self, instance):
        salesOrder = SalesOrder.objects.get(id=str(instance.salesOrderId.id))
        return SalesOrderBaiscSerializer(salesOrder).data

# class DeliverySerializer(serializers.ModelSerializer):
#     deliveryMan = serializers.SerializerMethodField()
#     class Meta:
#         model = PurchaseOrder
#         fields = [
#             'address',
#             'createdDate',
#             'purchaseOrderId',
#             'deliveryManId',
#             'deliveryMan',
#             'status'
#         ]
#     def get_deliveryMan(self, instance):
#         deliveryMan = DeliveryMan.objects.get(userId=str(instance.deliveryManId.userId.id))
#         return DeliveryManSerializer(deliveryMan).data

class SalesOrderSerializer(serializers.ModelSerializer):
    salesorder_salesorderitem = SalesOrderItemSerializer(read_only=True,many=True)
    user = serializers.SerializerMethodField()
    class Meta:
        model = SalesOrder
        fields = [
            'id',
            'paymentMethod',
            'createdDate',
            'clientId',
            'user',
            'salesorder_salesorderitem',
            'status',
            'rate',
            'address',
            'phone',
            'cost'
        ]
    def get_user(self, instance):
        user = User.objects.get(id=str(instance.clientId.userId.id))
        return UserSerializer(user).data
class NewOrderSerializer(serializers.ModelSerializer):
    neworder_neworderitem = NewOrderItemSerializer(read_only=True,many=True)
    user = serializers.SerializerMethodField()
    class Meta:
        model = NewOrder
        fields = [
            'id',
            'createdDate',
            'supplierId',
            'user',
            'neworder_neworderitem',
            'cost'
        ]
    def get_user(self, instance):
        user = User.objects.get(id=str(instance.supplierId.userId.id))
        return UserSerializer(user).data

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
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'price',
            'image',
            'amount',
            'isRawMaterial',
            'categoryId',
            'category',
            'item_rawmaterial',

        ]
    def get_category(self, instance):
        category = Category.objects.get(id=str(instance.categoryId.id))
        return CategoryBasicSerializer(category).data
    

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

# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Status
#         fields = [
#             'id',
#             'name',
#         ]

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

class DeliverySerializer(serializers.ModelSerializer):
    salesOrder = serializers.SerializerMethodField()
    deliveryMan = serializers.SerializerMethodField()
    class Meta:
        model = Delivery
        fields = [
            'id',
            'deliveryManId',
            'salesOrderId',
            'deliveryMan',
            'salesOrder'
        ]
    def get_deliveryMan(self, instance):
        deliveryMan = DeliveryMan.objects.get(userId=str(instance.deliveryManId.userId.id))
        return DeliveryManSerializer(deliveryMan).data
    def get_salesOrder(self, instance):
        salesOrder = SalesOrder.objects.get(id=str(instance.salesOrderId.id))
        return SalesOrderSerializer(salesOrder).data

class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = PurchaseOrdersItem
        fields = [
            'id',
            'quantity',
            'itemId',
            'purchaseOrderId',
            'item',
            "price"
        ]
    def get_item(self, instance):
        item = Item.objects.get(id=str(instance.itemId.id))
        return ItemSerializer(item).data

class PurchaseOrderSerializer(serializers.ModelSerializer):
    purcahase_purchaseorderitem = PurchaseOrderItemSerializer(read_only=True,many=True)
    user = serializers.SerializerMethodField()
    class Meta:
        model = PurchaseOrder
        fields = [
            'id',
            'createdDate',
            'supplierId',
            'user',
            'purcahase_purchaseorderitem',
            'cost'
        ]
    def get_user(self, instance):
        user = User.objects.get(id=str(instance.supplierId.userId.id))
        return UserSerializer(user).data

class RecipeSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    rawMaterial = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = [
            'id',
            'unit',
            'quantity',
            'itemId',
            'rawMaterialId',
            'item',
            'rawMaterial'
        ]
    def get_item(self, instance):
        item = Item.objects.get(id=str(instance.itemId.id))
        return ItemSerializer(item).data
    def get_rawMaterial(self, instance):
        rawMaterial = Item.objects.get(id=str(instance.rawMaterialId.id))
        return ItemSerializer(rawMaterial).data
