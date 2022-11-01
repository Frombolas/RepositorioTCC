from apps.autor.form import InsereAutor
from .models import Autor
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .form import InsereAutor

class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name: str = "autor/base.html"

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    fields = "__all__"
    template_name = "autor/update.html"
    success_url = "/autor/"

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = InsereAutor
    template_name = "criar.html"
    def form_valid(self, form):
        return super().form_valid(form)

#Deletar Usuário
class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/autor/"
    template_name = "autor/delete.html"

class AutorDetailView(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "autor/detail.html"