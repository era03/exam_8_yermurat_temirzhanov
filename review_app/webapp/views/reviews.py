from django.shortcuts import get_object_or_404, redirect
from webapp.forms import ReviewForm, Product
from webapp.models import Review

from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse




class ProductReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_create.html'


    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            rating = form.cleaned_data.get('rating')
            user = request.user
            Review.objects.create(author=user, product=product, text=text, rating=rating)
        return redirect('index')


class ReviewUpdateView(UpdateView):
    template_name = 'review_edit.html'
    form_class = ReviewForm
    model = Review
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('index')


class ReviewDeleteView(DeleteView):
    template_name = 'review_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')
    context_object_name = 'review'