from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


#New 
from django.http import JsonResponse
from .models import Product, Nutrition, Storage
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def product_list(request, product_type=None):
    if product_type:
        # Filter based on category name instead of ID
        storage_items = StorageItem.objects.filter(product_type=product_type)
    else:
        storage_items = StorageItem.objects.all()

    return render(request, 'product-list.html', {'storage_items': storage_items, 'category': product_type})


def product_detail(request, item_id):
    # Fetch the specific product by ID
    product = get_object_or_404(StorageItem, id=item_id)
    return render(request, 'product_detail.html', {'product': product})



def add_crop(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    try:
        farm = Farm.objects.get(farm_manager=user_profile)
    except Farm.DoesNotExist:
        farm = None

    if request.method == "POST":
        # If farm exists, show the crop form with that farm pre-selected
        if farm:
            crop_form = CropForm(request.POST)
            if crop_form.is_valid():
                crop = crop_form.save(commit=False)
                crop.farm = farm
                crop.save()
                return redirect('dashboard')  # Redirect to crop list after saving
        else:
            # If no farm exists for the user, prompt for farm creation
            farm_form = FarmForm(request.POST)
            crop_form = CropForm(request.POST)
            if farm_form.is_valid() and crop_form.is_valid():
                # Create a new farm and associate the user as the farm manager
                new_farm = farm_form.save(commit=False)
                new_farm.farm_manager = user_profile
                new_farm.save()

                # Create the crop and associate it with the newly created farm
                crop = crop_form.save(commit=False)
                crop.farm = new_farm
                crop.save()

                return redirect('dashboard')  # Redirect after saving
    else:
        # Create an empty crop form and farm form for GET request
        if farm:
            crop_form = CropForm()
        else:
            farm_form = FarmForm()  # Show farm creation form if no farm exists
            crop_form = CropForm()
        farm_form = FarmForm()  # Show farm creation form if no farm exists
        crop_form = CropForm()
    return render(request, 'add_crop_form.html', {'crop_form': crop_form, 'farm_form': farm_form, 'farm': farm})



def edit_crop(request, crop_id):
    crop = get_object_or_404(Crops, id=crop_id)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CropForm(instance=crop)
    return render(request, 'crop_edit_form.html', {'form': form})

def delete_crop(request, crop_id):
    crop = get_object_or_404(Crops, id=crop_id)
    if request.method == 'POST':
        crop.delete()
        return redirect('dashboard')
    return render(request, 'crop_confirm_delete.html', {'crop': crop})


def product_type(request):
    return render(request, "product-type.html") 


def edit_temp(request, product_id):
    product = get_object_or_404(StorageItem, id=product_id)

    if request.method == "POST":
        # Update temperature and humidity
        product.temperature = request.POST.get("temperature")
        product.humidity = request.POST.get("humidity")
        # product.product_quantity = product.product_quantity
        product.save()
        return redirect("dashboard")  # Redirect to the main dashboard after updating

    # Render the form with prepopulated data
    return render(request, "edit_temp.html", {"product": product})


def delete_item(request, item_id):
    # Get the item to delete or return a 404 if it doesn't exist
    item = get_object_or_404(StorageItem, id=item_id)
    item.delete()  # Delete the item

    return redirect('dashboard') 


#New line code for Nutritionist

# View for managing nutrition values of a specific product
def product_nutrition_management(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    nutrition, created = Nutrition.objects.get_or_create(product=product)

    if request.method == "POST":
        # Update nutrition values
        nutrition.calories = request.POST.get("calories")
        nutrition.protein = request.POST.get("protein")
        nutrition.carbohydrates = request.POST.get("carbohydrates")
        nutrition.fats = request.POST.get("fats")
        nutrition.comments = request.POST.get("comments")
        nutrition.save()
        return JsonResponse({"success": True, "message": "Nutritional values saved!"})

    return render(request, 'nutritionist_dashboard.html', {'product': product, 'nutrition': nutrition})

# Fetch products related to a specific storage
@csrf_exempt
def fetch_products_by_storage(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id)
    products = Product.objects.filter(storage=storage).values('id', 'name')
    return JsonResponse({"products": list(products)})


#For product deletation

from django.shortcuts import redirect, get_object_or_404
from .models import Product

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products')  

    return redirect('dashboard')





def add_productforfac(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    try:
        storage =  Storage.objects.get(storage_manager=user_profile)
    except Farm.DoesNotExist:
        storage = None

    if request.method == "POST":
        # If farm exists, show the crop form with that farm pre-selected
        if storage:
            crop_form = CropForm(request.POST)
            if crop_form.is_valid():
                crop = crop_form.save(commit=False)
                crop.farm = storage
                crop.save()
                return redirect('dashboard')  # Redirect to crop list after saving
        else:
            # If no farm exists for the user, prompt for farm creation
            farm_form = FarmForm(request.POST)
            crop_form = CropForm(request.POST)
            if farm_form.is_valid() and crop_form.is_valid():
                # Create a new farm and associate the user as the farm manager
                new_storage = farm_form.save(commit=False)
                new_storage.farm_manager = user_profile
                new_storage.save()

                # Create the crop and associate it with the newly created farm
                crop = crop_form.save(commit=False)
                crop.farm = new_storage
                crop.save()

                return redirect('dashboard')  # Redirect after saving
    else:
        # Create an empty crop form and farm form for GET request
        if storage:
            crop_form = CropForm()
        else:
            farm_form = FarmForm()  # Show farm creation form if no farm exists
            crop_form = CropForm()
        farm_form = FarmForm()  # Show farm creation form if no farm exists
        crop_form = CropForm()
    return render(request, 'add_crop_form.html', {'crop_form': crop_form, 'farm_form': farm_form, 'farm': storage})



def view_storage(request):
    # Your logic for the storage page
    return render(request, 'view_storage.html')


