from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'flickrsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^topten/', include('topten.urls', namespace="topten")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
