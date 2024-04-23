from . import views
from django.urls import path


urlpatterns = [
    path('diaries/new/', views.create_diary, name='create_diary'),
    path('', views.liked_posts, name='vinoteka'),
]
