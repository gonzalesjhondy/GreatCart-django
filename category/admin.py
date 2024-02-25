from django.contrib import admin
from .models import category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoryName',)} #this will automatic field up the slug if I type in categoryname input in django admin
    list_display = ('categoryName', 'slug') # 

admin.site.register(category, CategoryAdmin)