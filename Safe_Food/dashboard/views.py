from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from product.models import *


# Create your views here.
def n_report(request):
    return render(request, "n_report.html")


def nutrition_data(request):
    return render(request, "nutrition_data.html")


def dashboard(request):
    if(request.user.is_authenticated):
        user_type = request.user.UserProfile.user_type

        if(user_type == "qao"):
            return render(request, "quality_assurance_dashboard.html")
        
        elif(user_type == "fm"):
            return render(request,"farm_manager_dashboard.html")
        
        elif(user_type == "n"):
            return render(request, "nutritionist_dashboard.html")
        
        elif(user_type == "d"):
            return render(request,"distributor_dashboard.html")

        elif(user_type == "sm"):
            return render(request,"store_manager_dashboard.html")
        
        elif(user_type == "frm"):
            return render(request, "factory_manager_dashboard.html")
        
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
    

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")


def crop_management(request):
    # Fetch the UserProfile instance associated with the logged-in user
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    # Check if the user has a farm associated with them (as farm manager)
    if user_profile:
        try:
            farm = Farm.objects.get(farm_manager=user_profile)
        except Farm.DoesNotExist:
            farm = None
    else:
        farm = None

    # Filter crops based on the farm associated with the farm manager
    if farm:
        crops = Crops.objects.filter(farm=farm)  # Get crops related to the farm
    else:
        crops = Crops.objects.none()  # If no farm is found, show no crops

    return render(request, "crop_management.html", {'crops': crops})


def dt_product(request):
    return render(request, "dt_product.html")

def dt_shipment(request):
    return render(request, "shipments.html")