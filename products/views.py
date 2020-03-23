from django.shortcuts import render, redirect
from .forms import ProductForm,CategoryForm,RegisterForm
from .models import Product, Category
from django.views.generic import DetailView, UpdateView, ListView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#product CRUD
def list(request):
    products=Product.objects.all().order_by('-id')
    context={'products': products}
    return render(request,'products/list.html',context)



class ProductDetail(DetailView):
    model = Product

@login_required()
def createUpdateForm(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'products/product_form.html', {'form': form})
    else:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('products:list')


class ProductUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'products:detail'
    form_class = ProductForm
    model = Product

@login_required()
def product_delete(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('products:list')

#Categoy CRUD

def category_list(request):
    categories = Category.objects.all().order_by('-id')
    return  render(request, 'category/category_list.html',{'categories' : categories})

def create_category(request):
    form =  CategoryForm
    if request.method == 'POST':
        form= CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')

    return render(request,'category/category_create.html',{'form':form})

@login_required()
def update_category(request,id):
    category= Category.objects.get(id=id)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
        return redirect('products:category_list')
    return render(request,'category/category_update.html',{'category':category})
@login_required()
def delete_category(request,id):
    category= Category.objects.get(id=id)
    category.delete()
    return redirect('products:category_list')




#Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts/login/')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html',{'form':form})










