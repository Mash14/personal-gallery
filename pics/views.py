from django.shortcuts import render

from .models import Image,Category,Location

# Create your views here.

def image_list(request):
    images = Image.image_list()
    title = 'Home'
    return render(request, 'index.html',{"images":images,"title":title})