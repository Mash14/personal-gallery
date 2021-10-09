from django.http.response import Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Image,Category,Location

# Create your views here.

def image_list(request):
    images = Image.image_list()
    title = 'Home'
    return render(request, 'index.html',{"images":images,"title":title})

def single_image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    title = f'{{image_name}}'
    return render(request,'singe_image.html',{"image":image,"title":title})