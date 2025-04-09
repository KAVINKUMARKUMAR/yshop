from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
# Create your views here.
def homeView(request):
    template=loader.get_template('index.html')
    context={
        'products' : Product.objects.all()

    }
    return HttpResponse(template.render(context,request))

class ProductDetials(DetailView):
    model = Product
    template_name = 'product_details.html'
def aboutView(request):
    template=loader.get_template('about.html')
    context={

    }
    return HttpResponse(template.render(context,request))

def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context,request))


class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    fields = '__all__'
    success_url = '/'

class EditProduct(UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'edit_product.html'
    fields = ['img','price', 'stock', 'desc']
    success_url = '/'

class DelProduct(DeleteView):
    model = Product
    template_name = 'del_product.html'
    success_url = '/'