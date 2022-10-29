from django.views.generic import DetailView, UpdateView
from accounts.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


class UserChangePermissions(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().username == self.request.user or self.request.user.is_superuser

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        reviews = self.object.authors.order_by('rating')
        kwargs['reviews'] = reviews
        return super().get_context_data(**kwargs)


class UserChangeView(UserChangePermissions, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('index')


class UserPasswordChangeView(UserChangePermissions, UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('login')
