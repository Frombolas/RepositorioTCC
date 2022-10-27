from django.urls import path
from .views import TCCListView

urlpatterns = [
    path('', TCCListView.as_view(), name="listTCC"),
]