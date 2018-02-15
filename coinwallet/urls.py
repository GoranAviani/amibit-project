from django.conf.urls import url
from django.conf.urls import include
from coinwallet import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    url(r'^coinportfolio/create/', views.CoinWalletCreateView, name='coinportfolio_create'),
    url(r'^coinportfolio/dashboard/', views.CoinWalletDashboardView, name='coinportfolio_dashboard'),
    url(r'^coinportfolio/update/(?P<id>[0-9A-Za-z_\-]+)/', views.CoinWalletUpdateView, name='coinportfolio_update'),
    url(r'^coinportfolio/delete/(?P<id>[0-9A-Za-z_\-]+)/$', views.CoinWalletDeleteView, name='coinportfolio_delete'),

        ]
