from .models import TCC
from django.views.generic.list import ListView
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.urls import reverse_lazy
from .form import InsereTCC
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class TCCListView(ListView):
    model = TCC
    template_name: str = "list_t.html"
    paginate_by = 6

class TCCCreateView(LoginRequiredMixin, CreateView):
    model = TCC
    form_class = InsereTCC
    template_name = "criar.html"
    success_url = "/"
    def form_valid(self, form):
        return super().form_valid(form)
    
class TCCUpdateView(LoginRequiredMixin, UpdateView):
    model = TCC
    fields = "__all__"
    template_name = "update.html"
    success_url = "/"

#Deletar Usuário
class TCCDeleteView(LoginRequiredMixin, DeleteView):
    model = TCC
    success_url = "/"
    template_name = "delete.html"

class TCCDetailView(LoginRequiredMixin, DetailView):
    model = TCC
    template_name = "detail_t.html"