from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'department', 'role')
    search_fields = ('name', 'email', 'phone', 'department', 'role')