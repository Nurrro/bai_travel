from django.shortcuts import render
from .serializers import *
from rest_framework import generics, viewsets
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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



def main(request):
    carusel= Carusel.objects.all()
    hot_tours = HotTour.objects.all()
    otzyv = Otzyv.objects.all()
    photos = PhotoTours.objects.all()
    context = {'hottours':hot_tours, 'photos': photos, 'otzyv':otzyv, 'carusel':carusel}
    return render(request,'tour/index.html', context)

def tours(request):
    tour = Tours.objects.all()
    context = {'tour':tour}
    return render(request,"tour/tours.html", context)

def tour_detail(request,id):
    tour = Tours.objects.get(id=id)
    duration = tour.data_provedenya_end-tour.data_provedenya_start
    context = {'tour':tour, 'duration':duration }
    return render(request,'tour/tour-detail.html', context)

@csrf_exempt
def submit_form(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        number_of_people = request.POST.get("number_of_people")
        print(number_of_people)

        tour_id = request.POST.get('tour_id')

        zayavka = Zayavka(
            tour=Tours.objects.get(id=tour_id),
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            number_of_people=number_of_people
        )
        zayavka.save()
        print(zayavka.email)
        return JsonResponse({"message": "Форма успешно отправлена"}, status=200)
    else:
        return JsonResponse({"error": "Метод не поддерживается"}, status=405)

def about_us(request):
    context = {}
    return render(request,'tour/about-us.html', context)

def photos(request):
    photos = PhotoTours.objects.all()
    context = {'photos': photos}
    return render(request,'tour/photos.html', context)