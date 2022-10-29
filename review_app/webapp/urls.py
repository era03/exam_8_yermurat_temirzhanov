from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductDetailView, ProductCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'), 
]