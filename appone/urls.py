from django.conf.urls import url
from appone import views

app_name = 'appone'

urlpatterns = [
    url(r'^run/$', views.run, name='run'),
    url(r'^controller/$', views.controller, name='controller'),
    url(r'^delete_item/(?P<task_id>.+)/$', views.delete_item, name='delete_item'),
    url(r'^cancel_item/(?P<task_id>.+)/$', views.cancel_item, name='cancel_item')
]
