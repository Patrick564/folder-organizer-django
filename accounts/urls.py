from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'

urlpatterns = [
    path('create/', views.CreateAccountView.as_view(), name='create'),

    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='logout.html'
    ), name='logout'),
    path('change-password', auth_views.PasswordChangeView.as_view(
        # success_url='/',
        template_name='password_change.html'
    ), name='password-change'),
]
