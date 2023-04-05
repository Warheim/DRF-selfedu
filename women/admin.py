from django.contrib import admin
from women.models import Woman, Category


@admin.register(Woman)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_create', 'categories']
    list_filter = ['categories']


@admin.register(Category)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['name']
