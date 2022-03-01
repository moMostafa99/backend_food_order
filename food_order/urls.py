from django.urls import path
from . import views
urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),

    path('client/', views.ClientList.as_view()),
    path('client/<int:pk>', views.ClientDetail.as_view()),

    path('supplier/', views.SupplierList.as_view()),
    path('supplier/<int:pk>', views.SupplierDetail.as_view()),

    path('deliveryman/', views.DeliveryManList.as_view()),
    path('deliveryman/<int:pk>', views.DeliveryManDetail.as_view()),

    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),

    path('status/', views.StatusList.as_view()),
    path('status/<int:pk>', views.StatusDetail.as_view()),

    path('item/', views.ItemList.as_view()),
    path('item/<int:pk>', views.ItemDetail.as_view()),

    path('shoppingcart/', views.ShoppingCartList.as_view()),
    path('shoppingcart/<int:pk>', views.ShoppingCartDetail.as_view()),

    path('purchaseorder/', views.PurchaseOrderList.as_view()),
    path('purchaseorder/<int:pk>', views.PurchaseOrderDetail.as_view()),

    path('delivery/', views.DeliveryList.as_view()),
    path('delivery/<int:pk>', views.DeliveryDetail.as_view()),

    path('shippingorder/', views.ShippingOrderList.as_view()),
    path('shippingorder/<int:pk>', views.ShippingOrderDetail.as_view()),

    path('track/', views.TrackList.as_view()),
    path('track/<int:pk>', views.TrackDetail.as_view()),

    path('rawmaterial/', views.RawMaterialList.as_view()),
    path('rawmaterial/<int:pk>', views.RawMaterialDetail.as_view()),

    path('shoppingcartitem/', views.ShoppingCartItemList.as_view()),
    path('shoppingcartitem/<int:pk>', views.ShoppingCartItemDetail.as_view()),

    path('purchaseorderitem/', views.PurchaseOrderItemList.as_view()),
    path('purchaseorderitem/<int:pk>', views.PurchaseOrderItemDetail.as_view()),

    path('favorite/', views.FavoriteList.as_view()),
    path('favorite/<int:pk>', views.FavoriteDetail.as_view()),

    path('rate/', views.RateList.as_view()),
    path('rate/<int:pk>', views.RateDetail.as_view()),

    path('review/', views.ReviewList.as_view()),
    path('review/<int:pk>', views.ReviewDetail.as_view())
]