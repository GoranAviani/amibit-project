from .models import Link, Note
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import redirect



from datetime import datetime

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    )

from rest_framework.permissions import (
    IsAuthenticated,
    )

from .serializers import (
    LinkUpdateSerializer,
    )

from .forms import NoteCreate



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
        queryNote = Note.objects.all()
        return Response({'links': queryLink, 'notes':queryNote})
        #return Response()

class LinkCreateView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(link_user = self.request.user)



class LinkUpdateView(RetrieveUpdateAPIView): #retrieve is for detail view
    queryset = Link.objects.all()
    serializer_class = LinkUpdateSerializer
    lookup_field = 'id'
    def perform_update(self, serializer):
        serializer.save(link_user = self.request.user)

class LinkDestroyView(DestroyAPIView): #retrieve is for detail view
    queryset = Link.objects.all()
    lookup_field = 'id'

def NoteCreateView(request):
    if request.method == 'POST':
        form_note_create = NoteCreate(request.POST)
        if form_note_create.is_valid():
            #note_timestamp = datetime.datetime.now()
            note = form_note_create.save(commit=False)
            #null value in column "note_user_id" violates not-null constraint
            #DETAIL:  Failing row contains (18, commit=False, commit=False
            note.note_user = request.user
            note.save()
        return redirect('dashboard')
    else:
        form_note_create = NoteCreate()
    return render(request, 'note/note_create.html', {'form_note_create': form_note_create})
