from .models import Curso
from django.views.generic.list import ListView
from django.views.generic import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .form import InsereCurso

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name: str = "list_c.html"

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = InsereCurso
    success_url = "/curso/"
    template_name = "criar.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Curso"
        return data
    
class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = "__all__"
    template_name = "detail.html"
    success_url = "/curso/"

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = "/curso/"
    template_name = "delete.html"