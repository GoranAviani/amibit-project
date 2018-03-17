from django.conf.urls import url
from django.conf.urls import include
from linkmanager import views
from django.contrib.auth import views as auth_views


urlpatterns =[


   # url(r'^dashboard/', views.Dashboard.as_view(template_name="dashboard.html"),  name='dashboard'),
    url(r'^dashboard/', views.Dashboard,  name='dashboard'),

    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^termsandconditions', views.terms_and_conditions, name='terms_and_conditions'),

    url(r'^how_to/use', views.how_to_use, name='how_to_use'),
    url(r'^pa/listofcommands', views.pa_list_of_commands, name='pa_list_of_commands'),

    url(r'^link/create/', views.LinkCreateView, name='link_create'),
    url(r'^link/update/(?P<id>[0-9A-Za-z_\-]+)/$', views.LinkUpdateView, name='link_update'),
    url(r'^link/delete/(?P<id>[0-9A-Za-z_\-]+)/$', views.LinkDeleteView, name='link_delete'),

    url(r'^note/create/', views.NoteCreateView, name='note_create'),
<<<<<<< HEAD
    url(r'^note/update/(?P<id>.*)', views.NoteUpdateView, name='note_update'),
    url(r'^note/delete/(?P<id>.*)', views.NoteDeleteView, name='note_delete'),
=======
    url(r'^note/update/(?P<id>[0-9A-Za-z_\-]+)/', views.NoteUpdateView, name='note_update'),
    url(r'^note/delete/(?P<id>[0-9A-Za-z_\-]+)/', views.NoteDeleteView, name='note_delete'),
>>>>>>> 7d03cc46e1a67a27a63185adefd36d85f060e19e

    url(r'^user/login/', auth_views.login,  name='login'),
    url(r'^user/registration/', views.signup_view, name='register'),
    url(r'^user/logout/', views.logout_view, name='logout'),

	url(r'^user/setttings/', views.user_settings_menu, name='user_settings_menu'),
    url(r'^user/info/', views.user_info, name='user_info'),
	url(r'^user/infoedit/profile/', views.user_info_edit_profile, name='user_info_edit_profile'),
    url(r'^user/infoedit/password/', views.user_info_edit_password, name='user_info_edit_password'),

<<<<<<< HEAD
    url(r'^note/show/(?P<id>.*)/(?P<note_slug>.*)', views.note_detail, name='note_detail'),
=======
    url(r'^note/show/(?P<id>[0-9A-Za-z_\-]+)/(?P<note_slug>[0-9A-Za-z_\-]+)$', views.note_detail, name='note_detail'),
>>>>>>> 7d03cc46e1a67a27a63185adefd36d85f060e19e

        ]
