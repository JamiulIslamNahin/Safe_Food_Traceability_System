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
    # path('fm-overview', views.fm_overview, name = "fm_overview"),
    path('crop-management', views.crop_management, name = "crop_management"),
    # path('send-to-storage/<int:crop_id>/', views.send_to_storage, name='send_to_storage'),
    path('dt-product', views.dt_product, name = "dt_product"),
    path('dt-shipment', views.dt_shipment, name = "dt_shipment"), 
]
