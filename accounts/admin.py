from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'Lastname', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'Lastname')
    readonly_fields = ('last_login', 'date_joined') #fields will readonly
    ordering = ('-date_joined',)

    filter_horizontal = ()#this will set the password readOnly in django admin
    list_filter = ()#this will set the password readOnly in django admin
    fieldsets = ()#this will set the password readOnly in django admin

admin.site.register(Account, AccountAdmin) # this is reguster model

