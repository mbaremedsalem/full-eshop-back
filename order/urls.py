from django.urls import path
from .views import *
urlpatterns = [
    path('orders/new/', new_order, name="new_order"),
    path('orders/', get_orders, name="get_orders"),
    path('orders/<str:pk>/', get_order, name="get_order"),
    path('orders/<str:pk>/process/', process_order, name="process_order"),
    path('orders/<str:pk>/delete/', delete_order, name="delete_order"),

    path('create-checkout-session/', create_checkout_session, name="create_checkout_session"),
    path('order/webhook/', stripe_webhook, name="stripe_webhook"),

    
]
