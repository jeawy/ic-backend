from django.contrib import admin

# Register your models here.
from .models import Broker

@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone','address', 'company', 'license_no')
    search_fields = ('first_name', 'last_name', 'email', 'phone')