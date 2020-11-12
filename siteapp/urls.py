from django.urls import path
from siteapp import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^xml/',views.xml,name='xml'),
    url(r'^output/',views.output,name='output'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)