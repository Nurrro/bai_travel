from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Tours(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название номера")
    description = models.TextField(verbose_name="Описание")
    price_of_tour = models.IntegerField(verbose_name="Цена номера")
    discount = models.IntegerField(blank=True, null=True, verbose_name="Скидка в %")
    is_popular = models.BooleanField(default=False, verbose_name="Популярный номер?")

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        if self.discount:
            price = (self.price_of_tour / 100) * self.discount
            return self.price_of_tour - price
        return self.price_of_tour

    @property
    def photo(self):
        photo = self.photos.exists()
        if photo:
            return self.photos.first().photo
        return None
    
    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"   


class Carusel(models.Model):
    photo = models.ImageField(upload_to='uploads_carusel', verbose_name="Фото")
    title = models.CharField(max_length=65, verbose_name="Заголовок")
    content = models.CharField(max_length=255, verbose_name="Описание")
    
    def __str__(self):
       return self.title
    class Meta:
        verbose_name = "Главный фон"
        verbose_name_plural = "Главный фон"



class PhotoTours(models.Model):
    photo = models.ImageField(upload_to='uploads/images/')
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name="photos")

    def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.resize_image(self.photo)
        super().save(*args, **kwargs)

    def resize_image(self, image, size=(800, 600)):
        img = Image.open(image)
        img = img.resize(size, Image.Resampling.LANCZOS)

        img_io = BytesIO()
        img.save(img_io, format='JPEG')
        img_io.seek(0)

        new_image = InMemoryUploadedFile(img_io, None, image.name, 'image/jpeg', img_io.tell(), None)
        return new_image
    
    class Meta:
        verbose_name = "Фото Номера"
        verbose_name_plural = "Фотографии комнат"



class Otzyv(models.Model):
    photo = models.ImageField(upload_to='uploads/images/', null=True, verbose_name="Фотография")
    author = models.CharField(max_length=100, verbose_name="Автор")
    content = models.TextField(verbose_name="Отзыв")
    created_at = models.DateField(auto_created=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Отзыв от {self.author}"

    def save(self, *args, **kwargs):
        if self.photo:
            self.photo = self.resize_image(self.photo)
        super().save(*args, **kwargs)

    def resize_image(self, image, size=(800, 600)):
        img = Image.open(image)
        img = img.resize(size, Image.Resampling.LANCZOS)

        img_io = BytesIO()
        img.save(img_io, format='JPEG')
        img_io.seek(0)

        new_image = InMemoryUploadedFile(img_io, None, image.name, 'image/jpeg', img_io.tell(), None)
        return new_image
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"   
