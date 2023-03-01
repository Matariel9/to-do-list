from django.contrib import admin
from core import models

class UserAdmin(admin.ModelAdmin):
    search_fields = ('last_name', 'first_name','email','username',)
    list_filter = ['is_staff', 'is_active', 'is_superuser']
    list_display = ['username', 'email', 'first_name', 'last_name']

# Register your models here.
admin.site.register(models.User, UserAdmin)

