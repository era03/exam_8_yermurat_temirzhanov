from webapp.models import Product
from django.views.generic import ListView



class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1