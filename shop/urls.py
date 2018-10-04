from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
  path('', views.all_products, name='all_products'),
  # path('<slug:c_slug>/', views.all_paintings, name='paintings_by_category')
  path('commission/', views.commission, name='commission'),
  path('fineart/<slug:product_slug>/', views.product_detail, name='product_detail')
]