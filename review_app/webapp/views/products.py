from django.shortcuts import get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product, Review
from django.db.models import Avg

from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse




class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avarage = Review.objects.filter(product=self.object.id).aggregate(avg=Avg('rating'))
        context['avarage'] = avarage
        return context


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('index')


class ProductUpdateView(UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('index')


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    context_object_name = 'product'