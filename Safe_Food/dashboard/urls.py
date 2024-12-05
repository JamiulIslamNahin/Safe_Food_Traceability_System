from django.urls import path
from . import views
# from .forms import CropsForm


urlpatterns = [
    path('nutritionist-report', views.n_report, name = "n_report"),
    path('nutrition-data', views.nutrition_data, name = "nutrition_data"),  
    # path('nutritionist-dashboard', views.nutritionist_dashboard, name="nutritionist_dashboard"),
    # path('store-manager-dashboard', views.store_manager_dashboard, name="store_manager_dashboard"),
    path('admin-dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('', views.dashboard, name = "dashboard"),
    path('fm-overview', views.fm_overview, name = "fm_overview"),
    path('fm-report', views.fm_report, name = "fm_report"),
    path('fm-inventory', views.fm_inventory, name = "fm_inventory"),
    path('crop-management', views.crop_management, name = "crop_management"),
    path('dt-product', views.dt_product, name = "dt_product"),
    path('dt-shipment', views.dt_shipment, name = "dt_shipment"),
    # path('', views.crops_list, name='crops_list'),
    # path('create/', views.crops_create, name='crops_create'),
    # path('update/<int:pk>/', views.crops_update, name='crops_update'),
    # path('delete/<int:pk>/', views.crops_delete, name='crops_delete'),   
]
