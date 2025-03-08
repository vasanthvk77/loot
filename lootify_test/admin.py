from django.contrib import admin
from .models import Song  # Import your Song model

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'image', 'audio')  # Fields to display in admin panel
