"""food_order_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from food_order.models import *
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.models import Group as groupAdmin 
from django.contrib.auth.models import User as userAdmin

admin.site.unregister(groupAdmin)
admin.site.unregister(userAdmin)

admin.site.site_header = "Food Order Admin Panel"
admin.site.site_url = ""

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name","phone","email","userType"]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["userId"]

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["userId"]

@admin.register(DeliveryMan)
class DeliveryManAdmin(admin.ModelAdmin):
    list_display = ["userId"]

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ["userId"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","categoryId"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name","price","amount","isRawMaterial","image","categoryId"]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['itemId', 'unit', 'quantity', 'rawMaterialId']

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ["clientId"]

@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ["paymentMethod","createdDate","clientId",'address', 'status', 'phone', 'cost', 'rate']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["createdDate","supplierId", 'cost']

@admin.register(NewOrder)
class NewOrderAdmin(admin.ModelAdmin):
    list_display = ["createdDate","supplierId", 'cost']

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ["itemId","rawMaterialItemId"]

@admin.register(ShoppingCartItem)
class ShoppingCartItemAdmin(admin.ModelAdmin):
    list_display = ["quantity","itemId","shoppingCartId"]

@admin.register(SalesOrderItem)
class SalesOrderItemAdmin(admin.ModelAdmin):
    list_display = ["quantity","itemId","salesOrderId"]

@admin.register(PurchaseOrdersItem)
class PurchaseOrdersItemAdmin(admin.ModelAdmin):
    list_display = ["quantity","itemId","purchaseOrderId", "price"]

@admin.register(NewOrdersItem)
class NewOrdersItemAdmin(admin.ModelAdmin):
    list_display = ["quantity","itemId","newOrderId"]

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["clientId","itemId"]

@admin.register(Delivery)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["deliveryManId","salesOrderId"]

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^', include('food_order.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns = format_suffix_patterns(urlpatterns)
