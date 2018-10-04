from django.contrib import admin
from .models import Category, Painting

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = { 'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

# class TagAdmin(admin.ModelAdmin):
#   list_display = ['name', 'slug']
#   prepopulated_fields = { 'slug':('name',)}

# admin.site.register(Tag, TagAdmin)

class PaintingAdmin(admin.ModelAdmin):
  list_display = ['name', 'created', 'updated']
  prepopulated_fields = {'slug':('name',)}
  list_per_page = 20

admin.site.register(Painting, PaintingAdmin)
