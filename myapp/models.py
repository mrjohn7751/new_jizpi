from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Ekran Rasmi

class ekranImages(models.Model):
    name = models.CharField( max_length=50)
    img = models.ImageField(upload_to='Photos/ekran_IMG/',)

    class Meta:
        verbose_name = "Ekran Rasmi"
        verbose_name_plural ="Ekran Rasmlari"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ekranImages_detail", kwargs={"pk": self.pk})

# Category Yangiliklar (News)

class CategoryNews(models.Model):
    title = models.CharField( max_length=100,verbose_name='Kategoriya nomi')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("CategoryNews_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name="Maqolalar Kategoryasi"
        verbose_name_plural="Maqolalar Kategoryasi"
    
    
class ArticleNews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE)
    title = models.CharField( max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='Tana qismi')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    img1 = models.ImageField(blank=True, default=True, upload_to='Photos/Yangiliklar/',)
    img2 = models.ImageField(blank=True, default=True, upload_to='Photos/Yangiliklar/',)
    img3 = models.ImageField(blank=True, default=True, upload_to='Photos/Yangiliklar/',)
    created_at = models.DateTimeField( auto_now_add=True)
   
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ArticleNews_details", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["-id"]
        verbose_name="Maqola"
        verbose_name_plural="Maqolalar"
        
    

# Category Elon


class CategoryElon(models.Model):
    title = models.CharField( max_length=100,verbose_name='Kategoriya nomi')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("CategoryElon_detail", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name="Elonlar Kategoryasi"
        verbose_name_plural="Elonlar Kategoryasi"
    
    
class ArticleElon(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE)
    title = models.CharField( max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='Tana qismi')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ArticleElon_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["-id"]
        verbose_name="Elon"
        verbose_name_plural="Elonlar"
        