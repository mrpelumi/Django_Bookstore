from django.urls import path
from . import views

app_name = 'Carts'
urlpatterns = [
    path('',views.cart,name='cart'),
    path('cart-update/',views.update_cart,name='cart-update'),
    path('display-cart/',views.display_cart,name='display-cart'),
    path('clear-cart/',views.clear_cart,name='clear-cart'),
    path('stripe-page/',views.stripe_page,name='stripe-page'),
    path('config/', views.stripe_config,name='config'),
    path('create-checkout-session/', views.create_checkout_session,name='checkout_session'),
]