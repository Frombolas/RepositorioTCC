from multiprocessing import context
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .form import CadastroForm 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User 
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateView(CreateView):
    form_class = CadastroForm
    template_name = 'criar.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "email", "first_name", "last_name"]
    template_name = "profile.html"
    success_url = "/"

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = "/"
    template_name = "delete.html"

class PasswordView(LoginRequiredMixin, PasswordChangeView):
    model = User
    success_url = "/"
    template_name = "criar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["botao"] = "Nova Senha"
        context["title"] = "Modificar Senha"
        context["descricao"] = "Modificar Senha"

        return context    