from django.urls import path
from . import views

app_name='painting'

urlpatterns = [
  path('', views.home, name='fine_art_home'),
  path('all/', views.all_paintings, name='all_paintings'),
  path('artdemos/', views.art_demos, name='art_demos'),
  path('about/', views.about, name='about'),
  path('<slug:c_slug>/', views.all_paintings, name='paintings_by_category'),
]