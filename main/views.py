from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Maibyna Khairanisya',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)