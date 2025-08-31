from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # request.FILES для загрузки изображений
        if form.is_valid():  # Проверка формы на корректность
            form.save()  # Сохранение в базу данных
            return redirect('product_list')  # Перенаправление после успешного добавления
    else:
        form = ProductForm()

    return render(request, 'catalog/add_product.html', {'form': form})


def edit_product(request, product_id):
    # Получаем товар по ID или возвращаем 404, если товар не найден
    product = get_object_or_404(Product, product_id=product_id)

    if request.method == 'POST':
        # Передаем данные и файлы (если есть) в форму, используя instance для обновления существующего товара
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('product_list')  # Перенаправляем на страницу каталога
    else:
        # Заполняем форму текущими данными товара
        form = ProductForm(instance=product)

    # Рендерим шаблон с формой и контекстом
    return render(request, 'catalog/edit_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    # Получаем товар по ID или возвращаем 404, если товар не найден
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()  # Удаляем товар
        return redirect('product_list')  # Перенаправляем на страницу каталога

    # Рендерим шаблон с подтверждением удаления
    return render(request, 'catalog/delete_product.html', {'product': product})
    

def product_list(request):
    products = Product.objects.all()  # Получаем все товары
    return render(request, 'catalog/product_list.html', {'products': products})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'catalog/add_category.html', {'form': form})


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Перенаправление после сохранения
    
    else:
        form = CategoryForm(instance=category)  # Заполняем форму текущими данными
    
    return render(request, 'catalog/edit_category.html', {'form': form, 'category': category})


def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    
    return render(request, 'catalog/delete_category.html', {'category': category})
       

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


@login_required  # Доступ только авторизованным
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user.is_superuser and user != request.user:  # Только админ может удалять | # Нельзя удалить себя
        user.delete()
    
    return redirect('user_list')


def admin_dashboard(request):
    context = {
        'categories_count': Category.objects.count(),
        'products_count': Product.objects.count(),
        'users_count': User.objects.count(),
    }
    return render(request, 'main.html', context)