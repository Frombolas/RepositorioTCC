from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TCC

class TCCListView(ListView):
    model = TCC
    template_name: str = "tcc/teste.html"