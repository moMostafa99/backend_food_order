from django.db import models

# Create your models here.

def item_picture_path(instance, filename):
    return '/items/'.format(filename)

#Basic Data

class User(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=20,default='',blank=True, null=True)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=50,default='',blank=True, null=True)
    userType = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Client(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_client')
    def __str__(self):
        return str(self.userId.name)

class Supplier(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_supplier')
    def __str__(self):
        return str(self.userId.name)

class DeliveryMan(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_deliveryman', blank=True)
    def __str__(self):
        return str(self.userId.name)

class AdminUser(models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user_adminuser', blank=True)
    def __str__(self):
        return str(self.userId.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    categoryId = models.ForeignKey('self', on_delete=models.CASCADE, related_name='category_subcategory', blank=True, null=True)
    def __str__(self):
        return str(self.name)
    
class SalesOrder(models.Model):
    paymentMethod = models.TextField()
    createdDate = models.CharField(max_length=30, null=True)
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_salesorder')
    address = models.TextField(null=True)
    status = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=20,default='',blank=True, null=True)
    cost = models.FloatField(max_length=20,blank=True, null=True)
    rate = models.IntegerField(null=True, default=0)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.IntegerField()
    isRawMaterial = models.BooleanField(default=False)
    image = models.FileField(upload_to="items/", blank=True, null=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_item')
    
class ShoppingCart(models.Model):
    clientId = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True, related_name='client_shoppingCart')


class PurchaseOrder(models.Model):
    createdDate = models.CharField(max_length=30, null=True)
    supplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_purchaseorder', null=True)
    cost = models.FloatField(max_length=20,blank=True, null=True)

class NewOrder(models.Model):
    createdDate = models.CharField(max_length=30, null=True)
    supplierId = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_neworder', null=True, blank=True)
    cost = models.FloatField(max_length=20,blank=True, null=True)

class RawMaterial(models.Model):
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_rawmaterial')
    rawMaterialItemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rawmaterialitem_rawmaterial')

class ShoppingCartItem(models.Model):
    quantity = models.FloatField()
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_shoppingcartitem')
    shoppingCartId = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='shoppingcart_shoppingcartitem')

class SalesOrderItem(models.Model):
    quantity = models.FloatField()
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_salesorderitem')
    salesOrderId = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='salesorder_salesorderitem', null=True)

class Favorite(models.Model):
    clientId = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_favorite')
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_favorite')

class Delivery(models.Model):
    salesOrderId = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name='salesOrder_delivery', null=True)
    deliveryManId = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE, related_name= 'deliveryMan_delivery')

class PurchaseOrdersItem(models.Model):
    quantity = models.FloatField(null=True)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_purchaseorderitem')
    purchaseOrderId = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='purcahase_purchaseorderitem', null=True)
    price = models.FloatField(null=True)

class NewOrdersItem(models.Model):
    quantity = models.FloatField(null=True)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_neworderitem')
    newOrderId = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='neworder_neworderitem')

class Recipe(models.Model):
    quantity = models.IntegerField()
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_recipy')
    rawMaterialId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rawMaterial_recipy', null=True)
    unit = models.CharField(max_length=30)

