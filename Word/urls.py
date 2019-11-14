from . import views
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.Word, name='get-all-words'),
]   
