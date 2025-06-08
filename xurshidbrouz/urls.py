from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def robots_txt(request):
    if request.get_host().split(':')[0] == 'admin.xurshidbro.uz':
        return HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')
    # Optionally serve the normal robots.txt for the main domain
    return HttpResponse('User-agent: *\nAllow: /', content_type='text/plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('', include('blog.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 