from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from product.models import *
from product.forms import *


# Create your views here.
def n_report(request):
    return render(request, "n_report.html")


# def nutrition_data(request):
#     return render(request, "nutrition_data.html")
def products_information(request):
    # Fetch all products inherited from Storage
    products = Crops.objects.all()
    return render(request, 'nutrition_data.html', {'products': products })

def dashboard(request):
    if(request.user.is_authenticated):
        user_type = request.user.UserProfile.user_type

        if(user_type == "qao"):
            return render(request, "quality_assurance_dashboard.html")
        
        elif(user_type == "fm"):
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

            return render(request, "farm_manager_dashboard.html", {'crops': crops})
            # return render(request,"farm_manager_dashboard.html")
        
        elif(user_type == "n"):
            product_id = request.GET.get("product_id")
            product = Crops.objects.filter(id=product_id).first()
            return render(request, "nutritionist_dashboard.html", { "product": product })
        
        elif(user_type == "d"):
            return render(request,"distributor_dashboard.html")

        elif(user_type == "sm"):
            try:
                # Fetch the storage associated with the logged-in manager
                storage = Storage.objects.get(store_manager=request.user.UserProfile)
                # Fetch stored items for that storage
                stored_items = StorageItem.objects.filter(storage=storage)
            except Storage.DoesNotExist:
                stored_items = []  # If no storage is found for the user

            product_names = [item.product_name for item in stored_items]  # Assuming 'Crop_name' is the product name field
            product_quantities = [item.product_quantity for item in stored_items]
            context = {
                'stored_items': stored_items,
                'product_names': product_names,
                'product_quantities': product_quantities,
            }
            return render(request,"store_manager_dashboard.html", context)
        
        elif(user_type == "frm"):
            return render(request, "factory_manager_dashboard.html")
        
        elif(user_type =="ad"):
            return render(request,"admin_dashboard.html")
        
    else:
        return redirect(reverse('signin') + '?next=' + request.path)
    



def dt_product(request):
    return render(request, "dt_product.html")

def dt_shipment(request):
    return render(request, "shipments.html")



def view_farms(request):
    farms = Farm.objects.all()
    return render(request, "view_farms.html", {"farms": farms})

def view_farm_items(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    crops = Crops.objects.filter(farm=farm)
    return render(request, "view_farm_items.html", {"farm": farm, "crops": crops})


def add_to_storage(request, crop_id):
    crop = get_object_or_404(Crops, id=crop_id)
    user = request.user

    # Ensure the user is a store manager and fetch their associated storage
    try:
        storage = Storage.objects.get(store_manager__user=user)
    except Storage.DoesNotExist:
        return redirect("assign_storage")  # Redirect to the assign storage page

    if request.method == "POST":
        form = AddToStorageForm(request.POST)
        if form.is_valid():
            storage_item = form.save(commit=False)
            storage_item.storage = storage  # Assign the user's storage
            storage_item.crop = crop
            storage_item.save()

            # Set crop quantity to 0
            crop.Quantity = 0
            crop.save()

            return redirect("dashboard")
    else:
        form = AddToStorageForm()

    return render(request, "add_to_storage.html", {"form": form, "crop": crop, "storage": storage})



def assign_storage(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    if request.method == "POST":
        if "assign_storage" in request.POST:
            assign_form = AssignStorageForm(request.POST)
            if assign_form.is_valid():
                selected_storage = assign_form.cleaned_data["storage"]
                selected_storage.store_manager = user_profile
                selected_storage.save()
                return redirect("dashboard")  # Redirect to the dashboard after assignment
        elif "add_storage" in request.POST:
            add_form = AddStorageForm(request.POST)
            if add_form.is_valid():
                # Create and assign the new storage
                new_storage = Storage.objects.create(
                    storage_name=add_form.cleaned_data["storage_name"],
                    capacity=add_form.cleaned_data["capacity"],
                    address=add_form.cleaned_data["address"],
                    owner_name=add_form.cleaned_data["owner_name"],
                    store_manager=user_profile,
                )
                return redirect("dashboard")  # Redirect to the dashboard after adding storage
    else:
        assign_form = AssignStorageForm()
        add_form = AddStorageForm()

    return render(
        request,
        "assign_storage.html",
        {"assign_form": assign_form, "add_form": add_form},
    )



def farm_list(request):
    farms = Farm.objects.all()
    return render(request, 'farm_list.html', {'farms': farms})

def storage_list(request):
    storages = Storage.objects.prefetch_related('crops', 'store_manager__user').all()
    return render(request, 'storage_list.html', {'storages': storages})