from django.urls import path
from siteapp import views
from django.conf.urls import url

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^xml/',views.xml,name='xml'),
]

