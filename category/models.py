from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField('photos/categories', blank=True)

    class Meta: #changing table name the make migrations after
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
            return reverse('products_by_category', args=[self.slug]) #bring the urls category with the use of reverse function  enables retrieval of the url information
    
    def __str__(self): 
        return self.categoryName