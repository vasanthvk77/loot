
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import SongViewSet

# router = DefaultRouter()
# router.register(r'songs', SongViewSet)  # API endpoint for songs

# urlpatterns = [
#     path('', include(router.urls)),  # Includes all API routes
# ]

from django.urls import path
from .views import get_songs, upload_song

urlpatterns = [
    path('songs/', get_songs, name='get_songs'),
    path('songs/upload/', upload_song, name='upload_song'),
]
