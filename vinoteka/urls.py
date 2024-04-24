from . import views
from .views import DiaryDeleteView
from django.urls import path


urlpatterns = [
    path('diaries/new/', views.create_diary, name='create_diary'),
    path('diaries/<int:pk>/', views.diary_detail, name='diary_detail'),
    path('diaries/', views.diary_list, name='diary_list'),
    path('diary/<int:pk>/delete/', DiaryDeleteView.as_view(), name='diary_delete'),
    path('', views.liked_posts, name='vinoteka'),
]
