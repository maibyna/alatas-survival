from django.shortcuts import render,  redirect   # Tambahkan import redirect di baris ini
from main.forms import SurvivalEntryForm
from main.models import SurvivalEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    survival_entries = SurvivalEntry.objects.all()
    context = {
        'name': 'Maibyna Khairanisya',
        'class': 'PBP B',
        'survival_entries' : survival_entries
    }

    return render(request, "main.html", context)

def create_survival_entry(request):
    form = SurvivalEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
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