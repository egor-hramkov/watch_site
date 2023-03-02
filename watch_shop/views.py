from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from forms import RegisterUserForm, LoginUserForm, RegisterOrder, FilterForm
from .models import Watch, Basket, Orders


def mainpage(request):
    data = {
        "title": "EWatch"
    }
    return render(request, 'mainpage.html', context=data)


def watches_list(request):
    watches = Watch.objects.all()
    filter_form = FilterForm

    if request.method == 'POST':
        filter_form = FilterForm(request.POST)
        if filter_form.is_valid():
            price_start = filter_form.cleaned_data.get('price_start') if filter_form.cleaned_data.get('price_start') else 0
            price_end = filter_form.cleaned_data.get('price_end') if filter_form.cleaned_data.get('price_end') else 99999999
            watches = watches.filter(price__gte=price_start, price__lte=price_end)

            if filter_form.cleaned_data.get('is_water_resist'):
                watches = watches.filter(is_water_resist=True)

            if filter_form.cleaned_data.get('manufacturer'):
                watches = watches.filter(manufacturer__name=filter_form.cleaned_data.get('manufacturer'))

            if filter_form.cleaned_data.get('belt_type'):
                watches = watches.filter(manufacturer__name=filter_form.cleaned_data.get('belt_type'))

            if filter_form.cleaned_data.get('gender'):
                watches = watches.filter(gender=filter_form.cleaned_data.get('gender'))

    paginator = Paginator(watches, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'filter_form': filter_form,
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


@login_required()
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'user': user,
        'title': 'Ваш профиль',
    }
    return render(request, 'profile.html', context=context)


@login_required()
def basket(request):
    basket = Basket.objects.filter(user=request.user.id)
    total_price = 0
    for b in basket:
        total_price += b.product.price
    context = {
        'basket': basket,
        'total_price': total_price,
        'title': 'Корзина',
    }
    return render(request, 'basket.html', context=context)


@login_required()
def add_to_basket(request):
    product_id = request.query_params.get('product_id')
    Basket.objects.create(user=request.user.id, product=Watch.objects.get(id=product_id), amount=1)
    return redirect('get_watch', pk=product_id)


@login_required()
def delete_from_basket(request):
    product_id = request.query_params.get('product_id')
    Basket.objects.filter(user=request.user.id, product=Watch.objects.get(id=product_id)).delete()
    return redirect('basket')


@login_required()
def orders(request):
    orders = Orders.objects.filter(user=request.user.id)
    context = {
        'orders': orders,
        'title': 'Заказы',
    }
    return render(request, 'orders.html', context=context)


# @login_required()
# def get_order(request, pk):
#     order = Orders.objects.filter(id=pk, user=request.user)
#     if not order:
#         raise Http404
#     context = {
#         'order': order,
#         'title': 'Заказы',
#     }
#     return render(request, 'get_order.html', context=context)


@login_required()
def order_register(request):
    form = RegisterOrder
    if request.method == 'POST':
        form = RegisterOrder(request.POST)
        if form.is_valid():
            fields = form.save(commit=False)
            fields.user = User.objects.get(id=request.user.id)
            fields.save()
            return redirect('orders')

    if request.query_params.get('all'):
        objects = Basket.objects.filter(user=request.user.id)
    else:
        objects = Basket.objects.filter(product=request.query_params.get('product_id'))

    total_price = 0
    for obj in objects:
        total_price += obj.product.price

    context = {
        'objects': objects,
        'form': form,
        'title': 'Создание заказа',
        'total_price': total_price,
    }
    return render(request, 'register_order.html', context=context)


def pageNotFound(request, exception):
    context = {
        'title': 'Страница не найдена',
    }
    return HttpResponseNotFound(render(request, '404.html', context=context))
