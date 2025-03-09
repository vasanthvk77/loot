# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.http import JsonResponse
# from .models import Song
# from .serializers import SongSerializer

# # ✅ Fetch all songs
# @api_view(['GET'])
# def get_songs(request):
#     songs = Song.objects.all()
#     serializer = SongSerializer(songs, many=True)
#     return Response(serializer.data)

# # ✅ Upload a new song
# @api_view(['POST'])
# def upload_song(request):
#     serializer = SongSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

# # ✅ Custom 404 response for API endpoints

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Song
from .serializers import SongSerializer

# ✅ Fetch all songs
@api_view(['GET'])
def get_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

# ✅ Upload a new song (FIXED)
@api_view(['POST'])
def upload_song(request):
    # ✅ Ensure files are in request.FILES
    if 'image' not in request.FILES or 'audio' not in request.FILES:
        return Response({"error": "Image and audio files are required."}, status=400)

    data = request.data.copy()  # Make a mutable copy of request data
    data['image'] = request.FILES['image']  # Attach image file
    data['audio'] = request.FILES['audio']  # Attach audio file

    serializer = SongSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# ✅ Custom 404 response for API endpoints
def custom_api_404(request, exception):
    return JsonResponse({"error": "API endpoint not found."}, status=404)
