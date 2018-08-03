from django.contrib import admin
from django.urls import path
from .views import instaprova

urlpatterns = [
    path('instaprova/', instaprova),
    path('admin/', admin.site.urls),
]
