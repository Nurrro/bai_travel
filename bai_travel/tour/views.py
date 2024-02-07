from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from .models import *


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer   


class HotTourViewSet(viewsets.ModelViewSet):
    queryset = HotTour.objects.all()
    serializer_class = HotTourSerializer

class ZayavkaViewSet(viewsets.ModelViewSet):
    queryset = Zayavka.objects.all()
    serializer_class = ZayavkaSerializer

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class OtzyvViewSet(viewsets.ModelViewSet):
    queryset = Otzyv.objects.all()
    serializer_class = OtzyvSerializer

class CaruselViewSet(viewsets.ModelViewSet):
    queryset = Carusel.objects.all()
    serializer_class = CaruselSerializer
