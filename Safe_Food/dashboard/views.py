from django.shortcuts import render

# Create your views here.
def product_report(request):
    return render(request, "product_report.html")


def nutrition_data(request):
    return render(request, "nutrition_data.html")


def nutritionist_dashboard(request):
    return render(request, "nutritionist_dashboard.html")

def store_manager_dashboard(request):
    return render(request,"store_manager_dashboard.html")

def admin_dashboard(request):
    return render(request,"admin_dashboard.html")