from django.urls import path, include
from .views import *

urlpatterns = [
    path('province/', ProvinceView.as_view(), name='province'),
    path('department/', DepartmentView.as_view(), name='department'),
    path('municipality/', MunicipalityView.as_view(), name='municipality'),
    path('shops/', ShopView.as_view(), name='shops'),
    path('shop/<int:pk>', ShopByIdView.as_view(), name='shopById'),
    path('products/', ProductView.as_view(), name='products'),
    path('shelves/', ShelveView.as_view(), name='shelves'),
    path('shop-shelves/', ShopShelveView.as_view(), name='shop-shelves'),
    path('shop-shelves/<int:shop_id>', ShelvesByShopView.as_view(), name='shopShelvesByShop'),
    path('shelve-products/', ShelveProductView.as_view(), name='shelve-products'),
    path('shelve-products/<int:id>', ShelveProductByShopView.as_view(), name='shelveProducts'),

    path('roles/', RoleView.as_view(), name='roles'),
    path('clients/', ClientView.as_view(), name='clients'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
