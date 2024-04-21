from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

