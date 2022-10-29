from webapp.forms import ProductForm
from webapp.models import Product, Review
from django.db.models import Avg
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class GroupPermissions(UserPassesTestMixin):

    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists() or self.request.user.is_superuser


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avarage = Review.objects.filter(product=self.object.id).aggregate(avg=Avg('rating'))
        context['avarage'] = avarage
        return context


class ProductCreateView(GroupPermissions, LoginRequiredMixin, CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    model = Product
    groups = ['Moderator']

    def get_success_url(self):
        return reverse('index')


class ProductUpdateView(GroupPermissions, LoginRequiredMixin, UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    groups = ['Moderator']

    def get_success_url(self):
        return reverse('index')


class ProductDeleteView(GroupPermissions, LoginRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    context_object_name = 'product'
    groups = ['Moderator']