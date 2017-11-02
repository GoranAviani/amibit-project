from .models import Link, Note
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect


from django.utils import timezone
import datetime

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    )
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .permissions import *

from django.contrib.auth import (
    authenticate, #user = authenticate(username=user.username, password=raw_password)
    login,
    logout,
    update_session_auth_hash,
)

from .serializers import (
    LinkUpdateSerializer,
    )
from django.contrib.auth.forms import PasswordChangeForm

from .forms import (
LinkCreateForm,
NoteUpdateForm,
NoteDeleteForm,
UserRegisterForm,
UserInfo,
)


import webbrowser
HTTP_URL="http://"


#basic views:

def index(request):

    if request.user.is_authenticated():
        return redirect('dashboard')
    else:
    # Render the HTML template index.html with the data in the context variable
        return render(
            request,
            'index.html',
            #context={'num_apps':num_apps,'num_users':num_users},
            )
def about(request):
    return render(
    request,
    'perasis/about.html'
    )
def how_to_use(request):
    return render(
    request,
    'perasis/how_to_use.html'
    )


def pa_list_of_commands(request):
    return render(
    request,
    'perasis/pa_list_of_commands.html'
    )

def user_settings_menu(request):

     return render(
         request,
        'user/user_settings_menu.html',
    )

def user_info(request):
    #current_user ={'user': request.user}
    return render(request,'user/user_info.html')

#Api views:

#class Dashboard(APIView):
#    permission_classes=(IsAuthenticated,)
#    renderer_classes = [TemplateHTMLRenderer]
#    template_name = 'dashboard.html'
#
 #   def get(self, request):
 #       queryLink = Link.objects.filter(link_user=self.request.user)
 #       queryNote = Note.objects.filter(note_user=self.request.user)
 #       return Response({'links': queryLink, 'notes':queryNote})
        #return Response()
#dashboard:
def Dashboard(request):
    if request.user.is_authenticated():
        if(request.POST.get('personal_assistant_textbox')):
            text = request.POST.get('personal_assistant_textbox')
       
           #browser
            if text[0:2+1] == "go ":                
                return redirect(HTTP_URL+text[3:])

            elif text[0:3+1] == "goo ":
                return redirect(HTTP_URL+"www.google.com/?#q="+(text[4:]))    
            else:
                webbrowser.Error
            return redirect('dashboard')
        else:
            queryLink = Link.objects.filter(link_user=request.user)
            queryNote = Note.objects.filter(note_user=request.user)
            return render(request, 'dashboard.html', {
            'queryLink': queryLink,
            'queryNote': queryNote,
            })
    else:
        return render(request,'perasis/not_authenticaded.html')





######## Commented because with Rest its harder to add custom code
#class LinkCreateView(CreateAPIView):
#    queryset = Link.objects.all()
#    serializer_class = LinkUpdateSerializer
#    permission_classes=(IsAuthenticated,)
#    def perform_create(self, serializer):
#        serializer.save(link_user = self.request.user)

def LinkCreateView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_link_create = LinkCreateForm(request.POST)
            if form_link_create.is_valid():
                form = form_link_create.save(commit=False)
                form.link_user = request.user
                form.save()
            return redirect('dashboard')
        else:
            form_link_create = LinkCreateForm()
            return render(request, 'link/link_create.html', {'form_link_create': form_link_create})
    else:
        return render(request,'perasis/not_authenticaded.html')




class LinkUpdateView(RetrieveUpdateAPIView): #retrieve is for detail view
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer
    lookup_field = 'id'
    permission_classes= (IsAuthenticated,IsLinkOwner,)

    def perform_update(self, serializer):
            serializer.save(link_user = self.request.user)

class LinkDestroyView(DestroyAPIView): #retrieve is for detail view
    permission_classes= (IsAuthenticated,IsLinkOwner)
    queryset = Link.objects.all()
    lookup_field = 'id'


    #def get(self, request,id):
    #    lookup_field = 'id'
    #    queryset = Link.objects.filter(link_user=self.request.user)

#form views:
def NoteCreateView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_note_create = NoteCreate(request.POST)
            if form_note_create.is_valid():
                #note_timestamp = datetime.datetime.now()
                note = form_note_create.save(commit=False)
                note.note_user = request.user
                note.save()
            return redirect('dashboard')
        else:
            form_note_create = NoteCreate()
            return render(request, 'note/note_create.html', {'form_note_create': form_note_create})
    else:
        return render(request,'perasis/not_authenticaded.html')

def NoteUpdateView(request,id):
    note_to_update = get_object_or_404(Note, id=id)
    if request.user.is_authenticated():
        if note_to_update.note_user == request.user:
            if request.method == 'POST':
                form_note_update = NoteUpdateForm(request.POST)
                if form_note_update.is_valid():
                    note = form_note_update.save(commit=False)
                    note.id = id
                    note.note_timestamp = datetime.datetime.now()
                    note.note_user = request.user
                    note.save()
                    return redirect('dashboard')
            else:
                form_note_update = NoteUpdateForm(instance = note_to_update)
                return render(request, 'note/note_update.html', {'form_note_update': form_note_update})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        return render(request,'perasis/not_authenticaded.html')


def NoteDeleteView(request,id):
    note_to_delete = get_object_or_404(Note, id=id)
    if request.user.is_authenticated():
        if note_to_delete.note_user == request.user:
            if request.method == 'POST':
                form_note_delete = NoteDeleteForm(request.POST)
                if form_note_delete.is_valid():
                    note_to_delete.delete()
                    return redirect('dashboard')
            else:
                form_note_delete = NoteUpdateForm(instance=note_to_delete)
                return render(request, 'note/note_delete.html', {'form_note_delete': form_note_delete})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        return render(request,'perasis/not_authenticaded.html')
# kad se klikne na delete da izbaci pop up.
#alert()
#tk inter library za heroje
#if noute-user == request.user
#slik


def logout_view(request):
    logout(request)
    return render(request,"index.html",{})

#registration user:
def signup_view(request):
    if request.method == 'POST':
       form_signup = UserRegisterForm(request.POST)
       if form_signup.is_valid():
            user = form_signup.save()
            user.refresh_from_db()
            user.save()
            raw_password = form_signup.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form_signup = UserRegisterForm()
    return render(request, 'user/registration.html', {'form_signup': form_signup})

#edit user info:
def user_info_edit_profile(request):
    if request.method == 'POST':
        user_info_form = UserInfo(request.POST, instance = request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return redirect('user_info')
    else:
        user_info_form = UserInfo(instance=request.user)
        return render (request, 'user/user_info_edit_profile.html', {'user_info_form' : user_info_form})

#change user password:
def user_info_edit_password(request):
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(data = request.POST, user = request.user)

        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            return redirect('user_info')
    else:
        change_password_form=PasswordChangeForm(user = request.user)
        return render (request, 'user/user_change_password.html', {'change_password_form' : change_password_form})







#checkforHTTP()#########################
#def checkforHTTP(text):
#    pass
   # if text[0:2+1] == "go ":
   #     if text[4:10] == "http://":
   #         fixtext= text[11:0]
    #    return text




#checkforHTTP()