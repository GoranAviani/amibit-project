from .models import Link, Note
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render


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

    #def post(self, request):
    #    queryLink = Link.objects.all()
    #    queryNote = Note.objects.all()
    #    return Response({'links': queryLink, 'notes':queryNote})
