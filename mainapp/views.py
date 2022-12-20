from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello world!")

def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")