
from django.urls import path
from . import views

urlpatterns = [
    path('', views.source_list, name='source_list'),
    path('new/', views.source_create, name='source_create'),
    path('<int:pk>/edit/', views.source_edit, name='source_edit'),
    path('<int:pk>/delete/', views.source_delete, name='source_delete'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/new/', views.note_create, name='note_create'),
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
]
