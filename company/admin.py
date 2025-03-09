from django.contrib import admin
from .models import Company

# Register your models here.
@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone')