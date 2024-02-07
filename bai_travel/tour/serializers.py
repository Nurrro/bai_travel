from rest_framework import serializers
from .models import *

class PhotoToursSerailizer(serializers.ModelSerializer):
    class Meta:
        model = PhotoTours
        fields = ("photo",)

class HotTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotTour
        fields = "__all__"

class ZayavkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zayavka
        fields = "__all__"

class CaruselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carusel
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    photos = PhotoToursSerailizer(many=True)
    class Meta:
        model = Tours
        fields = ("id","name","description","data_provedenya_start","data_provedenya_end","place","price_of_tour","discount","discount_price","total_people","schetchik_zayavok","photos")




class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"


class OtzyvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otzyv
        fields = "__all__"
        
