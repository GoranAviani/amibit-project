from django.conf.urls import url
from django.conf.urls import include
from coinwallet import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    url(r'^coinwallet/create/', views.CoinWalletCreateView, name='coinwallet_create'),
    url(r'^coinwallet/dashboard/', views.CoinWalletDashboardView, name='coinwallet_dashboard'),
    url(r'^coinwallet/update/(?P<id>[0-9A-Za-z_\-]+)/', views.CoinWalletUpdateView, name='coinwallet_update'),
    url(r'^coinwallet/delete/(?P<id>[0-9A-Za-z_\-]+)/$', views.CoinWalletDeleteView, name='coinwallet_delete'),

        ]
