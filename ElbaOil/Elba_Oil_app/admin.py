from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)

