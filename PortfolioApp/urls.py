from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='Home'),
    path('about/',about,name='About'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('cal/',cal,name='cal'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)