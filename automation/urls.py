from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^isday/', views.isday, name='isday'),
    url(r'^status/', views.status, name='status'),
    url(r'^$', views.index, name='index'),
]