from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('tours/', views.tours, name='tours'),
    path('tour_detail/<int:id>', views.tour_detail, name='tour_detail'),
    path('about_us/', views.about_us, name='about_us'),
    path('photos/', views.photos, name='photos'),
]