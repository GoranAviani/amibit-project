from django.contrib import admin

# Register your models here.
from linkmanager.models import Link,Note

admin.site.register(Link)
admin.site.register(Note)
