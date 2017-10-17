from .models import Link, Note
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

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
    #serializer_class = LinkUpdateSerializer #not needed?
    lookup_field = 'id'

def NoteCreateView(request):
    if request.method == 'POST':
       note_timestamp = datetime.datetime.now()
    #import pdb; pdb.set_trace()



    return render(
    request,
    'note/note_create.html'
    )
