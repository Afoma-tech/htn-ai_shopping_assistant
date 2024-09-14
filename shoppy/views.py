from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def shoppypage(request):
    template = loader.get_template('shoppy.html')
    return HttpResponse(template.render())
