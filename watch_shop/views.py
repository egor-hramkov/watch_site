from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from forms import RegisterUserForm, LoginUserForm
from .models import Watch


def mainpage(request):
    data = {
        "title": "EWatch"
    }
    return render(request, 'mainpage.html', context=data)


def watches_list(request):
    watches = Watch.objects.all()
    paginator = Paginator(watches, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj': page_obj,
        'paginator': paginator,
        "title": "Каталог часов",
        "watches": page_obj,
    }
    return render(request, 'watches_list.html', context=data)


@login_required
def get_watch(request, pk):
    try:
        watch = Watch.objects.get(id=pk)
    except Watch.DoesNotExist:
        raise Http404()

    data = {
        "title": watch.manufacturer.name + ' ' + watch.name,
        "watch": watch,
    }
    return render(request, 'watch.html', context=data)


def register(request):
    form = RegisterUserForm()
    error = ""
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('mainpage')

    context = {
        'form': form,
        'title': 'Регистрация',
    }
    return render(request, 'registration.html', context=context)


def auth(request):
    form = LoginUserForm
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return redirect('mainpage')
    context = {
        'form': form,
        'title': 'Вход',
    }
    return render(request, 'auth.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user,
        'title': 'Ваш профиль',
    }
    return render(request, 'profile.html', context=context)
