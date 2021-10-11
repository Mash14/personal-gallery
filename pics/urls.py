from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.image_list,name = 'imageIndex'),
    url('^image/(\d+)',views.single_image, name = 'singleImage'),
    url('^search/',views.search_results, name = 'searchResults'),
    url('^location/(?P<location>\w+)',views.location_images,name = 'location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)