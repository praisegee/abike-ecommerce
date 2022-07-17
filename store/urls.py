from django import views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.store, name="store"),
    path("login/", views.user_login, name="login"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("<str:product_id>/", views.product, name="product"),
]
