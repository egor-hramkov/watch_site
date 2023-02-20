from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Watch


def mainpage(request):
    data = {
        "title": "EWatch"
    }
    return render(request, 'mainpage.html', context=data)


def watches_list(request):
    watches = Watch.objects.all()
    paginator = Paginator(watches, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj': page_obj,
        'paginator': paginator,
        "title": "Каталог часов",
        "watches": page_obj,
    }
    return render(request, 'watches_list.html', context=data)


def get_watch(request):
    watch = Watch.objects.get_object_or_404(id=request.pk)
    data = {
        "title": "Часы" + watch.manufacturer.name + watch.name,
        "watch": watch,
    }
    return render(request, 'watches_list.html', context=data)
