from django.urls import path
from .views import *
urlpatterns = [
    path('products/', get_products ,name='products'),
    path('products/new/', new_product ,name='products'),
    path('product/<str:pk>/',get_product,name='products-detaile'),
    path('products/upload_images/', upload_product_images, name="upload_product_images"),
    path('product/<str:pk>/update/',update_product,name='products-update'),
    path('product/<str:pk>/delete/',delete_product,name='products-delete'),
    path('<str:pk>/reviews/',create_review,name='create_review'),
    path('<str:pk>/reviews/delete/',delete_review,name='delete_review'),

]
