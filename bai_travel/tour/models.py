from django.db import models

class Tours(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    data_provedenya_start = models.DateField()
    data_provedenya_end = models.DateField()
    total_people = models.IntegerField(null=True, blank=True)
    place = models.CharField(max_length=100)
    price_of_tour = models.IntegerField()
    discount = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    
    @property
    def schetchik_zayavok(self):
        bids=self.bids.filter(status=True)
        return bids.count()



    @property
    def discount_price(self):
        if self.discount:
            price = (self.price_of_tour/100)*self.discount
            return self.price_of_tour-price
        return self.price_of_tour
    @property
    def photo(self):
        return self.photos.first().photo

class Carusel(models.Model):
    photo = models.ImageField('uploads_carusel')
    title = models.CharField(max_length=65)
    content = models.CharField(max_length=255)



class PhotoTours(models.Model):
    photo = models.ImageField(upload_to='uploads/images/')
    tour = models.ForeignKey(Tours,on_delete=models.CASCADE,related_name="photos")


class HotTour(models.Model):
    tour = models.OneToOneField(Tours, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Горячий тур - {self.tour} "
    



class Zayavka(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE,related_name="bids")
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    number_of_people = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"Заявка на тур {self.tour.name} от {self.full_name}"

class GalleryImage(models.Model):

    image = models.ImageField(upload_to='gallery/')


class Otzyv(models.Model):
    photo = models.ImageField(upload_to='uploads/images/', null=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_created=True)

    def __str__(self):
        return f"Отзыв от {self.author}"
