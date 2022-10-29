from django.urls import path
from accounts.views.login import LoginView, logout_view
from accounts.views.register import RegisterView
from accounts.views.users import UserDetailView, UserChangeView, UserPasswordChangeView



urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/edit', UserChangeView.as_view(), name='user_edit'),
    path('user/<int:pk>/change/password', UserPasswordChangeView.as_view(), name='user_password_change')
]