from django.urls import path
from .views import UserCreateView, UserUpdateView, UserDeleteView, PasswordView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<pk>", UserUpdateView.as_view(), name="perfil"),
    path("delete/<pk>", UserDeleteView.as_view(), name="delete"),
    path("mudar_senha/<pk>", PasswordView.as_view(), name="senha"),
]