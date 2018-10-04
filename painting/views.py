from django.shortcuts import render, get_object_or_404
from .models import Category, Painting
from shop.models import Product

def home(request):
  try:
    products = Product.objects.filter(featured=True)
  except Exception as e:
    raise e
  return render(request, 'painting/home.html', {'products':products})

def all_paintings(request, c_slug=None):
  c_page = None
  paintings = None
  if c_slug != None:
    c_page = get_object_or_404(Category, slug=c_slug)
    paintings = Painting.objects.filter(category=c_page)
  else:
    paintings = Painting.objects.all()
  return render(request, 'painting/category.html', {'category': c_page, 'paintings':paintings})

def art_demos(request):
  return render(request, 'painting/art_demos.html')

def about(request):
  return render(request, 'painting/about.html')

