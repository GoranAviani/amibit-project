from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm



class LinkCreateForm(forms.ModelForm):
    link_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    link_url = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    class Meta:
        model = Link
        fields = (
            'link_name',
            'link_url',
            )

class LinkUpdateForm(forms.ModelForm):
    link_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    link_url = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    class Meta:
        model = Link
        fields = (
            'link_name',
            'link_url',
            )

class LinkDeleteForm(forms.ModelForm):
    link_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class':'note-title-input'}))
    link_url = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class':'note-title-input'}))

    class Meta:
        model = Link
        fields = (
            'link_name',
            'link_url',
            )


class NoteCreateUpdateForm(forms.ModelForm):
    note_title = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    note_text = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'note-text-input'}))

    class Meta:
        model = Note
        fields = (
            'note_title',
            'note_text',
            )



class NoteDeleteForm(forms.ModelForm):
    note_title = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class':'note-title-input'}))
    note_text = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class':'note-text-input'}))
    class Meta:
        model = Note
        fields = (
            'note_title',
            'note_text',
            )

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    #first_name = forms.CharField(help_text='Required')
    #last_name = forms.CharField(help_text='Required')
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'note-title-input'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'password-input'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'password-input'}))
    class Meta:
        model = User
        fields = (
            'username',
            #'first_name',
            #'last_name',
            'email',
            'password1',
            'password2',
            )

class UserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            )
