from django.contrib import admin
from .models import Administrator


# Register your models here.

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_per_page = 50
