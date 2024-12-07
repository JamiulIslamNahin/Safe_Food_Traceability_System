from django.urls import path
from . import views


urlpatterns = [
    path('product-list', views.product_list, name = "product_list"),
    path('add/', views.add_crop, name='add_crop'),
    path('edit/<int:crop_id>/', views.edit_crop, name='edit_crop'),
    path('delete/<int:crop_id>/', views.delete_crop, name='delete_crop'),
    path('product-type', views.product_type, name = "product_type"),    
]


