from django.conf.urls import url
from . import views
from . import ajax

urlpatterns = [
    url(r'^status/', ajax.status, name='status'),
    url(r'^$', views.index, name='index'),
    url(r'^set/(?P<id>\d+)/(?P<value>\d+)/$', ajax.set_execution_element, name='set_execution_element'),
    url(r'^set/(?P<value>\d+)/$', ajax.set_all_execution_elements, name='set_all_execution_elements'),
    url(r'^setauto/(?P<id>\d+)/$', ajax.set_execution_element_auto, name='set_execution_element_auto'),
    url(r'^setauto/$', ajax.set_all_execution_elements_auto, name='set_all_execution_elements_auto'),
]