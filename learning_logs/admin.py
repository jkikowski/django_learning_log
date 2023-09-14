from django.contrib import admin

# Register your models here.

from .models import Topic, Entry

admin.site.register(Topic) #umożliwia zarządzanie modelem przez witryne localhost:8000/admin
admin.site.register(Entry)