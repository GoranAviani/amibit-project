from django.contrib import admin

# Register your models here.
from linkmanager.models import Link,Note



class LinkAdmin(admin.ModelAdmin):
    list_display = ("link_name" , "link_url" , "link_user")
    list_filter = ("link_name", "link_url" , "link_user")
    search_fields= ("link_name","link_url")



class NoteAdmin(admin.ModelAdmin):
    list_display = ("note_title" , "note_timestamp" , "note_user")
    list_filter = ("note_title" , "note_timestamp" , "note_user")
    prepopulated_fields = {"note_slug": ("note_title",)}
    search_fields= ("note_title","note_text")
    ordering = ["note_timestamp",]

admin.site.register(Link, LinkAdmin)
admin.site.register(Note, NoteAdmin)
