from django.urls import path
from . import views


urlpatterns = [
    path('product-list', views.product_list, name = "product_list"),
    path('product-list/<int:product_type>/', views.product_list, name='product_type'),
    path('product-detail/<int:item_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_crop, name='add_crop'),
    path('edit/<int:crop_id>/', views.edit_crop, name='edit_crop'),
    path('delete/<int:crop_id>/', views.delete_crop, name='delete_crop'),
    path('product-type', views.product_type, name = "product_type"), 
    path("edit-temp/<int:product_id>/", views.edit_temp, name="edit_temp"),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),


    #New line
    
    path('product/<int:product_id>/nutrition/', views.product_nutrition_management, name="product_nutrition_management"),
    path('storage/<int:storage_id>/products/', views.fetch_products_by_storage, name="fetch_products_by_storage"),   
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    
]




