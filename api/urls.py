from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^list/users/', views.UserListView.as_view(), name='api_user_list'),
        ]
