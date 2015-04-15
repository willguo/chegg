from django.conf.urls import patterns, include, url
from . import views
from .views import getTopPhotos


urlpatterns = patterns('',
    url(r'^$', getTopPhotos, name='topphotos'),
    # url(r'^$', ImageListView.as_view(), name='home'),
)