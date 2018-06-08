
from django.conf.urls import url,include
from django.contrib import admin
from linkmanager import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^$', views.index,  name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('linkmanager.urls')),
    url(r'^', include('coinwallet.urls')),

]
