from django.db import models
from category.models import category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=255, unique=True)
    description  = models.TextField(max_length=500, blank=True)
    price        = models.IntegerField()
    Images       = models.ImageField(upload_to='photos/products')
    stock   	 = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(category, on_delete=models.CASCADE)#models.CASCADE will do if Model category deleted, the products attach to the categroy will deleted
    created_date = models.DateTimeField(auto_now_add=True)#sets the field value only when the instance is created.
    modefied_date= models.DateTimeField(auto_now=True)#updates the field value every time the instance is saved

    def get_url(self):
        return reverse('products_detail', args=[self.category.slug, self.slug]) #self means model Product category means field of Products slug means the model of category ->field slug

    def __str__(self):
        return self.product_name