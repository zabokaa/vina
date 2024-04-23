from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog.models import Post
from .models import Diary
from .forms import DiaryForm


@login_required
def liked_posts(request):
    posts = Post.objects.filter(likes=request.user)
    return render(request, 'vinoteka/liked_posts.html', {'posts': posts})


@login_required
def create_diary(request):
    diaries = Diary.objects.filter(user=request.user)
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diary_detail', pk=diary.pk)
    else:
        form = DiaryForm()
    return render(request, 'vinoteka/create_diary.html', {'form': form, 'diaries': diaries})
