from django.conf.urls.defaults import *

urlpatterns = patterns('django_odesk.auth.views',
    url(r'^login/$', 'login'),
    url(r'^authenticate/$', 'authenticate'),
    url(r'^callback/$', 'callback'),
    url(r'^logout/$', 'logout'),
)
