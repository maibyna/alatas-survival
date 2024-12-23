import datetime
from django.shortcuts import render,   get_object_or_404, redirect, reverse  # Tambahkan import redirect di baris ini
from main.forms import SurvivalEntryForm
from main.models import SurvivalEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    survival_entries = SurvivalEntry.objects.filter(user=request.user)
    last_login = request.COOKIES.get('last_login', 'No last login available')

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'survival_entries' : survival_entries,
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
        messages.error(request, "Invalid username or password. Please try again.")
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required
def create_survival_entry(request):
    form = SurvivalEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Simpan data dari form, tapi belum commit ke database
        survival_entry = form.save(commit=False)
        
        # Kaitkan entry ini dengan user yang sedang login
        survival_entry.user = request.user
        
        # Simpan survival_entry ke database
        survival_entry.save()
        
        # Redirect ke halaman utama setelah menyimpan data
        return redirect('main:show_main')

    # Render form untuk input name, prize, dan description di template
    context = {"form" : form}
    return render(request, "create_survival_entry.html", context)

@csrf_exempt
@require_POST
def add_survival_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    user = request.user

    new_entry = SurvivalEntry(
        name=name, price=price, description=description, user=user
    )
    new_entry.save()

    return HttpResponse(b"CREATED", status=201)

def edit_survival_entry(request, id):
    # Get mood entry berdasarkan id
    survival = SurvivalEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = SurvivalEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_survival_entry.html", context)

def delete_survival_entry(request, id):
    # Get mood berdasarkan id
    survival = SurvivalEntry.objects.get(pk = id)
    # Hapus mood
    survival.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = SurvivalEntry.objects.filter(user=request.user)
    #data = SurvivalEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required
def show_json(request):
    data = SurvivalEntry.objects.filter(user=request.user)
    #data = SurvivalEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = SurvivalEntry.objects.filter(user=request.user)
    #data = SurvivalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required
def show_json_by_id(request, id):
    data = SurvivalEntry.objects.filter(user=request.user)
    #data = SurvivalEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required
@csrf_exempt
def create_survival_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = SurvivalEntry.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            descrption=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
