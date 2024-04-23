from . import views
from django.urls import path


urlpatterns = [
    path('', views.liked_posts, name='vinoteka'),
]
