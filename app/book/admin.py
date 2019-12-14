from django.contrib import admin
from .models import Category, Book


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 50


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_per_page = 50
