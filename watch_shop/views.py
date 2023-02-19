from django.shortcuts import render

from .models import Watch


def mainpage(request):
    data = {
        "title": "EWatch"
    }
    return render(request, 'mainpage.html', context=data)


def watches_list(request):
    watches = Watch.objects.all()
    data = {
        "title": "Каталог часов",
        "watches": watches,
    }
    return render(request, 'watches_list.html', context=data)
