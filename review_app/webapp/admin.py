from django.contrib import admin
from webapp.models import Product, Review



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'image')
    list_filter = ('id', 'name', 'description', 'category')
    search_fields = ('name', 'description', 'category')
    fields = ('name', 'description', 'image', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'product', 'text', 'rating')
    list_filter = ('id', 'author', 'product', 'text', 'rating')
    search_fields = ('author', 'product', 'text', 'rating')
    fields = ('author', 'product', 'text', 'rating')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)