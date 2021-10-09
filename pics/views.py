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
    title = 'image'
    return render(request,'single_image.html',{"image":image,id: image_id,"title":title})

def search_result(request):
    if 'image_category' in request.GET and request.GET['image_category']:
        searched_category =  request.GET.get('image_category')
        images = Image.search_by_category(searched_category)
        message = f'{searched_category}'

        title = f'{searched_category}'
        return render(request, 'search.html', {'message': message,'images':images, 'title':title})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 