# src/tasks/frontend_urls.py
from django.urls import path
from .views import list_list, list_detail
from .views import label_list, label_detail

urlpatterns = [
    path('lists/',          list_list,   name='list_list'),
    path('lists/<int:pk>/', list_detail, name='list_detail'),
    path('labels/',          label_list,   name='label_list'),
    path('labels/<int:pk>/', label_detail, name='label_detail'),
]
