from django.db import models

# Create your models here.

def item_picture_path():
    return 'items/'

#Basic Data

class User(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=20,default='',blank=True, null=True)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=50,default='',blank=True, null=True)
    userType = models.CharField(max_length=20)
    provider = models.CharField(max_length=20, blank= True)
    def __str__(self):
        return str(self.name)

class Client(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_client')

class Supplier(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_supplier')

class DeliveryMan(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_deliveryman')

class Category(models.Model):
    name = models.CharField(max_length=200)
    categoryId = models.ForeignKey('self', on_delete=models.CASCADE, related_name='category_subcategory', blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.FloatField()
    isRawMaterial = models.BooleanField(default=False)
    description = models.CharField(max_length=2000)
    image = models.FileField(upload_to=item_picture_path, blank=True, null=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_item')
    
class ShoppingCart(models.Model):
    clientId = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, related_name='client_shoppingCart')

class PurchaseOrder(models.Model):
    paymentMethod = models.TextField()
    createdDate = models.DateTimeField()
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_purchaseorder')
    supplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_purchaseorder')

class Delivery(models.Model):
    district = models.TextField()
    streetName = models.TextField()
    building = models.IntegerField()
    floor = models.IntegerField()
    apartment = models.IntegerField()
    createdDate = models.DateTimeField()
    purchaseOrderId = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE, primary_key=True, related_name='purchaseorder_delivery')
    deliveryManId = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE, related_name='deliveryman_delivery')
    
class Track(models.Model):
    createdDate = models.DateTimeField()
    deliveryId = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='delivery_track')
    statusId = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_track')
    
#Many to Many

class RawMaterial(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_rawmaterial')
    rawMaterialItemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rawmaterialitem_rawmaterial')

class ShoppingCartItem(models.Model):
    quantity = models.FloatField()
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_shoppingcartitem')
    shoppingCartId = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='shoppingcart_shoppingcartitem')

class PurchaseOrderItem(models.Model):
    quantity = models.FloatField()
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_purchaseorderitem')
    purchaseOrderId = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purchaseorder_purchaseorderitem')

class Favorite(models.Model):
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_favorite')
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_favorite')

class Rate(models.Model):
    rate = models.FloatField()
    createdDate = models.DateTimeField()
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_rate')
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_rate')

class Review(models.Model):
    comment = models.TextField()
    createdDate = models.DateTimeField()
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_review')
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_review')