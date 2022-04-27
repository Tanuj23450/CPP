from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop1/', Shop1.as_view(), name='shop1'),
    path('shop2/', Shop2.as_view(), name='shop2'),
    path('shop3/', Shop3.as_view()),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('edit/', Edit, name='edit'),

    path('login/', Login, name='login'),
    path('signup/', SignUp, name='signup'),
    path('signup-shop', SignUp2, name='signup-shop'),
    path('logout/', Logout, name='logout'),

    path('search/', Search, name='search'),

    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product/<slug>/edit/', ItemEdit, name='editProd'),
    path('product/<slug>/edit/delete/', ItemDelete, name='delProd'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
] 

from django.contrib import admin