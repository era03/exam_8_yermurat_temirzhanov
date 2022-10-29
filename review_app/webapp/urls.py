from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'), 
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]