from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    url(r'^dashboard/', views.Dashboard.as_view(template_name="dashboard.html"),  name='dashboard'),
    url(r'^about', views.about, name='about'),
    url(r'^update/(?P<id>[0-9A-Za-z_\-]+)/$', views.LinkUpdateView, name='link_update'),
    ]
