from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =[
    url(r'^dashboard/', views.Dashboard.as_view(template_name="dashboard.html"),  name='dashboard'),
    url(r'^about', views.about, name='about'),
    url(r'^link/create/', views.LinkCreateView.as_view(), name='link_create'),
    url(r'^link/update/(?P<id>[0-9A-Za-z_\-]+)/$', views.LinkUpdateView.as_view(), name='link_update'),
    url(r'^link/delete/(?P<id>[0-9A-Za-z_\-]+)/$', views.LinkDestroyView.as_view(), name='link_delete'),
    url(r'^note/create/', views.NoteCreateView, name='note_create'),
    url(r'^note/update/(?P<id>[0-9A-Za-z_\-]+)/', views.NoteUpdateView, name='note_update'),
    url(r'^note/delete/(?P<id>[0-9A-Za-z_\-]+)/', views.NoteDeleteView, name='note_delete'),

    url(r'^user/login/', auth_views.login,  name='login'),
    url(r'^user/registration/', views.signup_view, name='register'),
    url(r'^user/logout/', views.logout_view, name='logout'),

	url(r'^user/setttings/', views.user_settings_menu, name='user_settings_menu'),
    url(r'^user/info/', views.user_info, name='user_info'),
	url(r'^user/infoedit/profile/', views.user_info_edit_profile, name='user_info_edit_profile'),


        ]
