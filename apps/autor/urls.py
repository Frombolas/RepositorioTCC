from django.urls import path
from .views import AutorListView, AutorUpdateView, AutorCreateView, AutorDeleteView, AutorDetailView

urlpatterns = [
    path('', AutorListView.as_view(), name="listAutor"),
    path('Autor/cria_autor', AutorCreateView.as_view(), name='criaAutor'),
    path('Autor/update/<pk>', AutorUpdateView.as_view(), name='updateAutor'),
    path('Autor/detail/<pk>', AutorDetailView.as_view(), name="detailAutor"),
    path('Autor/delete/<pk>', AutorDeleteView.as_view(), name="deleteAutor"),
]