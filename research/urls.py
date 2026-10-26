from django.urls import path
from . import views

urlpatterns = [
    path('', views.source_list, name='source_list'),
    path('new/', views.source_create, name='source_create'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/new/', views.note_create, name='note_create'),
]