from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def homeView(request):
    template=loader.get_template('index.html')
    context={

    }
    return HttpResponse(template.render(context,request))
def aboutView(request):
    template=loader.get_template('index.html')
    context={

    }
    return HttpResponse(template.render(context,request))