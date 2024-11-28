from django.shortcuts import render

# Create your views here.
def product_report(request):
    return render(request, "product_report.html")


def nutrition_data(request):
    return render(request, "prnutrition_data.html")


def nutritionist_dashboard(request):
    return render(request, "nutritionist_dashboard.html")