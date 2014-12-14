from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from dataclustering.views import home_view, make_kluster_view, instructions_view, myKlusters_view, insertcode_view, getjsonfromcode

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clusteringapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view),
    url(r'^makekluster', make_kluster_view),
    url(r'^instructions', instructions_view),
    url(r'^insertcode', insertcode_view),
    url(r'^myklusters', myKlusters_view),
    url(r'^getjsonfromcode', getjsonfromcode),
)
