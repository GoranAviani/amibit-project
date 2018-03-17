from django.conf.urls import url
from django.conf.urls import include
from coinwallet import views
from django.contrib.auth import views as auth_views


urlpatterns =[
<<<<<<< HEAD
    url(r'^coinportfolio/create/', views.CoinWalletCreateView, name='coinportfolio_create'),
    url(r'^coinportfolio/dashboard/', views.CoinWalletDashboardView, name='coinportfolio_dashboard'),
    url(r'^coinportfolio/update/(?P<id>[0-9A-Za-z_\-]+)/', views.CoinWalletUpdateView, name='coinportfolio_update'),
    url(r'^coinportfolio/delete/(?P<id>[0-9A-Za-z_\-]+)/$', views.CoinWalletDeleteView, name='coinportfolio_delete'),
=======
    url(r'^coinwallet/create/', views.CoinWalletCreateView, name='coinwallet_create'),
    url(r'^coinwallet/dashboard/', views.CoinWalletDashboardView, name='coinwallet_dashboard'),
    url(r'^coinwallet/update/(?P<id>[0-9A-Za-z_\-]+)/', views.CoinWalletUpdateView, name='coinwallet_update'),
    url(r'^coinwallet/delete/(?P<id>[0-9A-Za-z_\-]+)/$', views.CoinWalletDeleteView, name='coinwallet_delete'),
>>>>>>> 7d03cc46e1a67a27a63185adefd36d85f060e19e

        ]
