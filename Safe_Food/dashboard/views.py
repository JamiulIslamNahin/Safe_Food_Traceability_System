from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.
def n_report(request):
    return render(request, "n_report.html")


def nutrition_data(request):
    return render(request, "nutrition_data.html")


def dashboard(request):
    if(request.user.is_authenticated):
        user_type = request.user.UserProfile.user_type

        if(user_type == "qao"):
            pass
        elif(user_type == "fm"):
            return render(request,"farm_manager_dashboard.html")
        
        elif(user_type == "n"):
            return render(request, "nutritionist_dashboard.html")
        
        elif(user_type == "d"):
            return render(request,"distributor_dashboard.html")

        elif(user_type == "sm"):
            return render(request,"store_manager_dashboard.html")
        
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
    

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def fm_report(request):
    return render(request, "fm_reports.html")

def fm_inventory(request):
    return render(request, "fm_inventory.html")

def fm_overview(request):
    return render(request, "fm_overview.html")

def crop_management(request):
    return render(request, "crop_management.html")

def dt_product(request):
    return render(request, "dt_product.html")

def dt_shipment(request):
    return render(request, "shipments.html")