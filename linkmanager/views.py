from linkmanager.models import Link, Note
from django.contrib.auth.models import User


from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
import datetime


from django.contrib.auth import (
    authenticate, #user = authenticate(username=user.username, password=raw_password)
    login,
    logout,
    update_session_auth_hash,
)


from django.contrib.auth.forms import PasswordChangeForm

from linkmanager.forms import (
LinkCreateForm,
LinkUpdateForm,
LinkDeleteForm,
NoteCreateUpdateForm,
NoteDeleteForm,
UserRegisterForm,
UserInfo,
)


# Used for check does the link have http or https in the beginning
#In function add_HTTP_to_linkurl
HTTP_URL = "http://"
HTTPS_URL = "https://"


def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard')
    else:
        #Show how many users,notes,links there are on Amibit
        num_note = Note.objects.all().count()
        num_user = User.objects.count()
        num_link = Link.objects.count()

        return render(
            request,
            'index.html',
            context={'num_note': num_note, 'num_user':num_user, 'num_link': num_link},
            )
def about(request):
    return render(
    request,
    'perasis/about.html'
    )

def contact(request):
    return render(
    request,
    'perasis/contact.html'
    )


def terms_and_conditions(request):
    return render(
    request,
    'perasis/terms_and_conditions.html'
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
    return render(request,'user/user_info.html')

def Dashboard(request):
    if request.user.is_authenticated():
        #if PAbox has post
        if(request.POST.get('personal_assistant_textbox')):
            text = request.POST.get('personal_assistant_textbox')

            #According to first part of text in PAbox open second part of the PAbox
            if text[0:2+1] == "go ":
                return redirect(HTTP_URL+text[3:])

            elif text[0:3+1] == "goo ":
                return redirect(HTTP_URL+"www.google.com/?#q="+(text[4:]))
            elif text[0:3+1] == "ddg ":
                return redirect(HTTP_URL+"www.duckduckgo.com/?q="+(text[4:]))

            else:
                return redirect(HTTP_URL+"www.duckduckgo.com/?q="+(text))

            return redirect('dashboard')

        #If PAbox has not been posted display notes, links
        else:
            queryLink = Link.objects.filter(link_user=request.user).order_by('-id')
            queryNote = Note.objects.filter(note_user=request.user).order_by('-note_timestamp')
            return render(request, 'dashboard.html', {
            'queryLink': queryLink,
            'queryNote': queryNote,
            })
    else:
        #if user is not authenticated inform him of that
        return render(request, 'perasis/not_authenticaded.html')



def LinkCreateView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_link_create = LinkCreateForm(request.POST)
            if form_link_create.is_valid():
                form = form_link_create.save(commit=False)
                form.link_user = request.user
                #Check does the link have http or https in the beginning
                form.link_url = add_HTTP_to_linkurl(form.link_url)
                form.save()
                messages.success(request, 'Link saved!',extra_tags='link_create')
            return redirect('dashboard')
        else:
            form_link_create = LinkCreateForm()
            return render(request, 'link/link_create.html', {'form_link_create': form_link_create})
    else:
        # if user is not authenticated inform him of that
        return render(request,'perasis/not_authenticaded.html')


#Check does the link have http or https on the beginning, if it does not add it
def add_HTTP_to_linkurl(link_url):
    if link_url[0:7] != HTTP_URL:
        if link_url[0:8] != HTTPS_URL:
            link_url = HTTP_URL + link_url
    return link_url


def LinkUpdateView(request,id):
    link_to_update = get_object_or_404(Link, id=id)
    if request.user.is_authenticated():
        if link_to_update.link_user == request.user:
            if request.method == 'POST':
                form_link_update = LinkUpdateForm(request.POST)
                if form_link_update.is_valid():
                    link = form_link_update.save(commit=False)
                    link.id = id
                    link.link_user = request.user
                    # Check does the link have http or https in the beginning
                    link.link_url = add_HTTP_to_linkurl(link.link_url)
                    link.save()
                    return redirect('dashboard')
            else:
                form_link_update = LinkUpdateForm(instance = link_to_update)
                return render(request, 'link/link_update.html', {'form_link_update': form_link_update})
        else:
            return render(request, 'perasis/not_owner.html')
    else:
        # if user is not authenticated inform him of that
        return render(request,'perasis/not_authenticaded.html')



def LinkDeleteView(request,id):
    link_to_delete = get_object_or_404(Link, id=id)
    if request.user.is_authenticated():
        if link_to_delete.link_user == request.user:
            if request.method == 'POST':
                form_link_delete = LinkDeleteForm(request.POST)
                if form_link_delete.is_valid():
                    link_to_delete.delete()
                    return redirect('dashboard')
            else:
                form_link_delete = LinkDeleteForm(instance=link_to_delete)
                return render(request, 'link/link_delete.html', {'form_link_delete': form_link_delete})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        # if user is not authenticated inform him of that
        return render(request, 'perasis/not_authenticaded.html')


def check_for_unusual_characters(note_title):
    note_slug = ""
    note_slug=note_title
    for letter in note_title:
        if not letter.isalpha():
            note_slug=note_slug.replace(letter, "-")
    return note_slug

def check_note_input(form_data):
    if form_data.get('note_title') == "":
        form_data.update({'note_title': (form_data.get('note_text')[0:200:])})
    elif form_data.get('note_text') == "":
        form_data.update({'note_text': form_data.get('note_title')})
    return(form_data)    


def NoteCreateView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form_note_create = NoteCreateUpdateForm(request.POST)
            if form_note_create.is_valid():
                note = form_note_create.save(commit=False)
                note.note_user = request.user
                note.note_slug = check_for_unusual_characters(note.note_title)
                note.save()
                messages.success(request, 'Note saved!',extra_tags='note_create')
                return redirect('dashboard')
        else:
            form_note_create_update = NoteCreateUpdateForm()
            return render(request, 'note/note_create.html', {'form_note_create_update': form_note_create_update})
    else:
        # if user is not authenticated inform him of that
        return render(request,'perasis/not_authenticaded.html')

def NoteUpdateView(request,id):
    note_to_update = get_object_or_404(Note, id=id)
    if request.user.is_authenticated():
        if note_to_update.note_user == request.user:
            if request.method == 'POST':
                form_note_create_update = NoteCreateUpdateForm(request.POST)
                if form_note_create_update.is_valid():
                    note = form_note_create_update.save(commit=False)
                    note.id = id
                    note.note_timestamp = datetime.datetime.now()
                    note.note_user = request.user
                    note.note_slug = check_for_unusual_characters(note.note_title)
                    note.save()
                    return redirect('dashboard')
            else:
                form_note_create_update = NoteCreateUpdateForm(instance = note_to_update)
                #return render(request, 'note/note_update.html', {'form_note_update': form_note_update})
                return render(request, 'note/note_update.html', {'form_note_create_update': form_note_create_update})
                
        else:
            return render(request,'perasis/not_owner.html')
    else:
        # if user is not authenticated inform him of that
        return render(request, 'perasis/not_authenticaded.html')


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
                form_note_delete = NoteDeleteForm(instance=note_to_delete)
                return render(request, 'note/note_delete.html', {'form_note_delete': form_note_delete})
        else:
            return render(request,'perasis/not_owner.html')
    else:
        # if user is not authenticated inform him of that
        return render(request, 'perasis/not_authenticaded.html')

def logout_view(request):
    logout(request)
    return render(request,"index.html",{})

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
    return render(request, 'registration/registration.html', {'form_signup': form_signup})

def user_info_edit_profile(request):
    if request.method == 'POST':
        user_info_form = UserInfo(request.POST, instance = request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return redirect('user_info')
        else:
            user_info_form = UserInfo(instance=request.user)
            return render (request, 'user/user_info_edit_profile.html', {'user_info_form' : user_info_form})

    else:
        user_info_form = UserInfo(instance=request.user)
        return render (request, 'user/user_info_edit_profile.html', {'user_info_form' : user_info_form})

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
    else:
        change_password_form=PasswordChangeForm(user = request.user)
        return render (request, 'user/user_change_password.html', {'change_password_form' : change_password_form})


def note_detail(request,id,note_slug):
    note_to_show = get_object_or_404(Note, id=id, note_slug=note_slug)

    return render (request, "note/note_detail.html", {"note_to_show":note_to_show})
