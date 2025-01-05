from django.shortcuts import render
from .serializers import *
# from rest_framework import generics, viewsets
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    carusel= Carusel.objects.all()
    hot_tours = Tours.objects.filter(is_popular=True)
    otzyv = Otzyv.objects.all()
    photos = PhotoTours.objects.all()
    context = {'hottours':hot_tours, 'photos': photos, 'otzyv':otzyv, 'carusel':carusel}
    return render(request,'tour/index.html', context)

def some_view(request):
    context = {
        'canonical_url': request.build_absolute_uri()  # Генерирует текущий URL
    }
    return render(request, 'some_template.html', context)

def tours(request):
    tour = Tours.objects.all()
    context = {'tour':tour}
    return render(request,"tour/tours.html", context)

def tour_detail(request,id):    
    tour = Tours.objects.get(id=id)
    context = {'tour':tour, }
    return render(request,'tour/tour-detail.html', context)


def about_us(request):
    context = {}
    return render(request,'tour/about-us.html', context)

def photos(request):
    photos = PhotoTours.objects.all()
    context = {'photos': photos}
    return render(request,'tour/photos.html', context)