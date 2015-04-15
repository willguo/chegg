from django.conf.urls import patterns, include, url
from . import views
from .views import topPhotos

urlpatterns = [
    url(r'^$', topPhotos, name='index'),
]
