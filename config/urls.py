from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stories.urls')),
    path('sources/', include('research.urls')),
    path('tasks/', include('planning.urls')),
]