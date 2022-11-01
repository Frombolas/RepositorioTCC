from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import CadastroForm

class UserCreateView(CreateView):
    form_class = CadastroForm
    template_name = 'criar.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        return super().form_valid(form)