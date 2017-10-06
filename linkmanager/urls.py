from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    url(r'^$', views.index,  name='index'),
    url(r'^dashboard/', views.Dashboard.as_view(template_name="dashboard.html"),  name='dashboard'),
    url(r'^about', views.about, name='about'),
    ]
