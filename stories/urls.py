from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),
    path('new/', views.story_create, name='story_create'),
    path('topics/new/', views.topic_create, name='topic_create'),
    path('<int:pk>/', views.story_detail, name='story_detail'),
    path('<int:pk>/edit/', views.story_edit, name='story_edit'),
    path('<int:pk>/delete/', views.story_delete, name='story_delete'),
]