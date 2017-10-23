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
#from rest_framework.permissions import (
#    IsAuthenticated,
    #IsAuthenticatedOrReadOnly,
    #IsAuthenticatedAndOwner,
#    )
from rest_framework.permissions import *
from .permissions import *

from django.contrib.auth import (
    authenticate, #user = authenticate(username=user.username, password=raw_password)
    login,
    logout,
)

from .serializers import (
    LinkUpdateSerializer,
    )

from .forms import (
NoteCreate,
NoteUpdateForm,
NoteDeleteForm,
UserRegisterForm,
)



def index(request):
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


class Dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dashboard.html'

    def get(self, request):
        queryLink = Link.objects.filter(link_user=self.request.user)
        queryNote = Note.objects.filter(note_user=self.request.user)
        return Response({'links': queryLink, 'notes':queryNote})
        #return Response()

class LinkCreateView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer
    permission_classes=(IsAuthenticated)
    def perform_create(self, serializer):
        serializer.save(link_user = self.request.user)



class LinkUpdateView(RetrieveUpdateAPIView): #retrieve is for detail view
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer
    lookup_field = 'id'
    permission_classes= (IsAuthenticated,IsOwner,)

    def perform_update(self, serializer):
            serializer.save(link_user = self.request.user)

class LinkDestroyView(DestroyAPIView): #retrieve is for detail view
    permission_classes= (IsAuthenticated,IsOwner)
    queryset = Link.objects.all()
    lookup_field = 'id'
    permission_classes= (IsAuthenticated,IsOwner)

    #def get(self, request,id):
    #    lookup_field = 'id'
    #    queryset = Link.objects.filter(link_user=self.request.user)


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
    new_to_update = get_object_or_404(Note, id=id)
    if request.user.is_authenticated():
        if Note.note_user == request.user:
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
                form_note_update = NoteUpdateForm(instance = new_to_update)
                return render(request, 'note/note_update.html', {'form_note_update': form_note_update})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        return render(request,'perasis/not_authenticaded.html')


def NoteDeleteView(request,id):
    if request.user.is_authenticated():
        if Note.note_user == request.user:
            new_to_delete = get_object_or_404(Note, id=id)
            if request.method == 'POST':
                form_note_delete = NoteDeleteForm(request.POST)
                if form_note_delete.is_valid():
                    new_to_delete.delete()
                    return redirect('dashboard')
            else:
                form_note_delete = NoteUpdateForm(instance=new_to_delete)
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
    return render(request, 'users/registration.html', {'form_signup': form_signup})
