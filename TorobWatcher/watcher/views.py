from django.shortcuts import render
from django.http import HttpResponse
from . import watcher

def update_product_price(request):
    watcher.release_dogs()

    return HttpResponse('Price Updated')