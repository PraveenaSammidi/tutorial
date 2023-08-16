from django.contrib import admin
from .models import Members

# Register your models here.

@admin.register(Members)
class Memberadmin(admin.ModelAdmin):
    list_display = ['name','age','city']
