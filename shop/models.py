from django.db import models
from django.urls import reverse
# from imagekit.models import ImageSpecField
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill


class Category(models.Model):
  name = models.CharField(max_length=250, unique=True)
  slug = models.SlugField(max_length=250, unique=True)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='category', blank=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    # return '{}'.format(self.name)
    return self.name

class Tag(models.Model):
  name = models.CharField(max_length=250, unique=True)
  slug = models.SlugField(max_length=250, unique=True)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='category', blank=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'tag'
    verbose_name_plural = 'tags'

  def __str__(self):
    # return '{}'.format(self.name)
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=250, unique=True)
  slug = models.SlugField(max_length=250, unique=True)
  subtitle = models.CharField(max_length=350, blank = True, null = True)
  description = models.TextField(blank=True)
  category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank = True, null = True)
  tag = models.ManyToManyField(Tag)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='product')
  image1 = models.ImageField(upload_to='product', blank=True)
  image2 = models.ImageField(upload_to='product', blank=True)
  stock = models.IntegerField()
  available = models.BooleanField(default=True)
  featured = models.BooleanField(default=False)
  commission = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'product'
    verbose_name_plural = 'products'

  def get_url(self):
    return reverse('shop:product_detail', args=[self.slug])

  def __str__(self):
    # return '{}'.format(self.name)
    return self.name

# class Product_Image(models.Model):
#   product                 = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)    
#   product_image_created   = models.DateTimeField(auto_now_add=True)
#   product_image_updated   = models.DateTimeField(auto_now=True)
  
  
#   product_image           = ProcessedImageField(upload_to='product',
#                                                 processors=[ResizeToFill(400,400)],
#                                                 format='JPEG',
#                                                 options={'quality': 80})
  

#   class Meta:
#       ordering                = ('-product_image_created',)
#       verbose_name            = 'product-image'
#       verbose_name_plural     = 'products-images'
  
#   def __str__(self):
#       return '{}'.format(self.product_image)

