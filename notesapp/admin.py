from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'updated')

#if we don't do this we won't see this in the admin panel
admin.site.register(Note)