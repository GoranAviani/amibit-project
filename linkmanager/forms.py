from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class NoteCreate(forms.ModelForm):
    #your_name = forms.CharField(label='Your name', max_length=100)
    note_title = forms.CharField(help_text='Required')
    note_text = forms.CharField(help_text='Required')

    class Meta:
        model = Note
        fields = (
            #'note_user',
            'note_title',
            'note_text',
        #    'note_timestamp',
            )
