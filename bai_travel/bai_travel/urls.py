from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tour.views import *
from rest_framework import routers




router = routers.DefaultRouter()
router.register(r'tours', TourViewSet, basename='tours')
router.register(r'hot-tour', HotTourViewSet, basename='hot-tour')
router.register(r'zayavki', ZayavkaViewSet, basename='zayavki')
router.register(r'gallery', GalleryImageViewSet, basename='gallery')
router.register(r'otzyvy', OtzyvViewSet, basename='otzyvy')
router.register(r'carusel', CaruselViewSet, basename='carusel')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tour.urls")),
    path('api/v1/', include(router.urls)),

]



if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
