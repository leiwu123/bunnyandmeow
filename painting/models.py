from django.db import models
from django.urls import reverse

class Category(models.Model):
  name = models.CharField(max_length=250, unique=True)
  slug = models.SlugField(max_length=250, unique=True)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='category', blank=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def get_url(self):
    return reverse('painting:paintings_by_category', args=[self.slug])

  def __str__(self):
    # return '{}'.format(self.name)
    return self.name

# class Tag(models.Model):
#   name = models.CharField(max_length=250, unique=True)
#   slug = models.SlugField(max_length=250, unique=True)
#   description = models.TextField(blank=True)
#   image = models.ImageField(upload_to='category', blank=True)

#   class Meta:
#     ordering = ('name',)
#     verbose_name = 'tag'
#     verbose_name_plural = 'tags'

#   def __str__(self):
#     # return '{}'.format(self.name)
#     return self.name


class Painting(models.Model):
  name = models.CharField(max_length=250, unique=True)
  slug = models.SlugField(max_length=250, unique=True)
  dimension = models.CharField(max_length=250)
  description = models.TextField(blank=True)
  category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank = True, null = True)
  # tag = models.ManyToManyField(Tag)
  image = models.ImageField(upload_to='product')
  featured = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'painting'
    verbose_name_plural = 'paintings'

  def __str__(self):
    # return '{}'.format(self.name)
    return self.name
