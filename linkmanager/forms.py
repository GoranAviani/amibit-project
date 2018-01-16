from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm



class LinkCreateForm(forms.ModelForm):
    link_name = forms.CharField()
    link_url = forms.CharField()
    class Meta:
        model = Link
        fields = (
            'link_name',
            'link_url',
            )

class LinkUpdateForm(forms.ModelForm):
    link_name = forms.CharField()
    link_url = forms.CharField()
    class Meta:
        model = Link
        fields = (
            'link_name',
            'link_url',
            )

class LinkDeleteForm(forms.ModelForm):
    link_name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    link_url = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Link
        fields = (
            'link_name',
            'link_url',
            )


class NoteCreateForm(forms.ModelForm):
    #your_name = forms.CharField(label='Your name', max_length=100)
    note_title = forms.CharField()
    note_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Note
        fields = (
            #'note_user',
            'note_title',
            'note_text',
            #'note_timestamp',
            )


class NoteUpdateForm(forms.ModelForm):
    note_title = forms.CharField()
    note_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Note
        fields = (
            #'note_user',
            'note_title',
            'note_text',
        #    'note_timestamp',
            )
class NoteDeleteForm(forms.ModelForm):
    note_title = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    note_text = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Note
        fields = (
            #'note_user',
            'note_title',
            'note_text',
            #'note_timestamp',
            )

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(help_text = "Requireddd. 150 charachets of fever. Letters, digits and @/./+/-/_ only.")
    #first_name = forms.CharField(help_text='Required')
    #last_name = forms.CharField(help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Required. Type a valid email address.')
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput,help_text='Your password cant be too similar to your other personal information,must contain at least 8 characters.')
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
