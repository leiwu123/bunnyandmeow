from django.contrib import admin
from .models import Category, Tag, Product

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = { 'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = { 'slug':('name',)}

admin.site.register(Tag, TagAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price','stock', 'category', 'available', 'created', 'updated']
  list_editable = ['price', 'stock', 'available']
  prepopulated_fields = {'slug':('name',)}
  list_per_page = 20

admin.site.register(Product, ProductAdmin)

# admin.site.register(Product_Image)