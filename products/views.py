from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductForm, TypeProductForm
from .models import Product, TypeProduct


# Функция для проверки, является ли пользователь администратором
def is_admin(user):
    return user.groups.filter(name='Admin').exists()


# region work_with_product
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


@login_required
def product_list(request):
    products = Product.objects.all()
    types = TypeProduct.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'types': types})


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


# endregion

# region work_with_type
@login_required
def add_type_product(request):
    if request.method == 'POST':
        form = TypeProductForm(request.POST, request.FILES)  # Обработка файлов
        if form.is_valid():
            form.save()
            return redirect('type_product_list')
    else:
        form = TypeProductForm()
    return render(request, 'products/add_type_product.html', {'form': form})


@login_required
def type_product_list(request):
    types = TypeProduct.objects.all()
    return render(request, 'products/type_product_list.html', {'types': types})


@login_required
def type_product_detail(request, type_id):
    type_product = get_object_or_404(TypeProduct, id=type_id)
    return render(request, 'products/type_product_detail.html', {'type_product': type_product})


@login_required
def edit_type_product(request, type_id):
    type_product = get_object_or_404(TypeProduct, id=type_id)
    if request.method == 'POST':
        form = TypeProductForm(request.POST, request.FILES, instance=type_product)
        if form.is_valid():
            form.save()
            return redirect('type_product_detail', type_id=type_product.id)
    else:
        form = TypeProductForm(instance=type_product)
    return render(request, 'products/edit_type_product.html', {'form': form, 'type_product': type_product})
# endregion
