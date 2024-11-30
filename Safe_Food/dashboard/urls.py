from django.urls import path
from . import views


urlpatterns = [
    path('product-report', views.product_report, name = "product_report"),
    path('nutrition-data', views.nutrition_data, name = "nutrition_data"),  
    path('nutritionist-dashboard', views.nutritionist_dashboard, name="nutritionist_dashboard"),
    path('store-manager-dashboard', views.store_manager_dashboard, name="store_manager_dashboard"),
    path('admin-dashboard', views.admin_dashboard, name="admin_dashboard"),


]
