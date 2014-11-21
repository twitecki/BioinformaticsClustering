from django.conf.urls import patterns, include, url
from django.contrib import admin
from dataclustering.views import home_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clusteringapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view),
)
