from django.conf.urls import url
from . import views
from . import ajax

urlpatterns = [
    url(r'^status/', ajax.status, name='status'),
    url(r'^$', views.index, name='index'),
    url(r'^set/(?P<id>\d+)/(?P<value>\d+)/$', ajax.set_execution_element, name='set_execution_element'),
]