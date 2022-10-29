from django.urls import path
from webapp.views.base import IndexView
from webapp.views.products import ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from webapp.views.reviews import ProductReviewCreateView, ReviewUpdateView, ReviewDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'), 
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/confirm-delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/review/create', ProductReviewCreateView.as_view(), name='create_review'),
    path('review/<int:pk>/edit', ReviewUpdateView.as_view(), name='review_edit'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('review/<int:pk>/confirm-delete/', ReviewDeleteView.as_view(), name='review_confirm_delete'),

]