import datetime
from django.shortcuts import render,   get_object_or_404, redirect   # Tambahkan import redirect di baris ini
from main.forms import SurvivalEntryForm
from main.models import SurvivalEntry, Purchase, Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    survival_entries = SurvivalEntry.objects.all()
    purchases = Purchase.objects.filter(user=request.user)
    last_login = request.COOKIES.get('last_login', 'No last login available')
    
    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'survival_entries' : survival_entries,
        
        'purchases': purchases,

        
        'last_login': last_login,
    }

    return render(request, "main.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_available_products():
    return Product.objects.all()  # Mengambil semua produk dari database

@login_required
def create_survival_entry(request):
    form = SurvivalEntryForm(request.POST or None)
    
    # Mendapatkan semua produk dari database
    products = Product.objects.all()  # Gunakan model Product untuk mengambil produk yang tersedia dari database

    if request.method == "POST":
        product_id = request.POST.get("product_id")  # Mengambil product_id dari form
        quantity = request.POST.get("quantity")

        # Mendapatkan produk yang dipilih dari database menggunakan product_id
        selected_product = Product.objects.filter(id=product_id).first()

        if selected_product and quantity.isdigit() and int(quantity) > 0:
            # Simpan pembelian ke database
            Purchase.objects.create(
                user=request.user,
                product=selected_product,
                quantity=int(quantity),
                price=selected_product.price * int(quantity),
                description=selected_product.description
            )
            response = redirect('main:show_main')
            # Set cookie 'last_login' saat pembelian
            response.set_cookie('last_login', request.COOKIES.get('last_login', 'Data login tidak tersedia'))
            return response
            #return redirect('main:show_main')  # Redirect kembali ke halaman utama setelah pembelian

    context = {'products': products, 'form': form}
    return render(request, "create_survival_entry.html", context)


def show_xml(request):
    data = SurvivalEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = SurvivalEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = SurvivalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = SurvivalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
