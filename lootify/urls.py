from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse  # ✅ Import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

# ✅ Create a simple welcome page function
def home(request):
    return JsonResponse({"message": "Welcome to the Lootify API!"})

# ✅ Custom 404 handler
def custom_404(request, exception):
    return JsonResponse({"error": "The requested resource was not found."}, status=404)

urlpatterns = [
    path('', home),  # ✅ Add homepage route
    path('admin/', admin.site.urls),
    path('api/', include('lootify_test.urls')),  # ✅ Include your app URLs
]

# ✅ Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Set custom handler for 404 errors
handler404 = custom_404
