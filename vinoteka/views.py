from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from .models import Diary
from .forms import DiaryForm

def diary_detail(request, pk):
    diary = get_object_or_404(Diary, pk=pk)
    return render(request, 'vinoteka/diary_detail.html', {'diary': diary})

def diary_list(request):
    diaries = Diary.objects.filter(user=request.user)
    return render(request, 'vinoteka/diary_list.html', {'diaries': diaries})

@login_required
def liked_posts(request):
    posts = Post.objects.filter(likes=request.user)
    form = DiaryForm()  # create a DiaryForm instance and add form to the context
    diaries = Diary.objects.filter(user=request.user)
    return render(request, 'vinoteka/liked_posts.html', {'posts': posts, 'form': form, 'diaries': diaries})


@login_required
def create_diary(request):
    diaries = Diary.objects.filter(user=request.user)
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('vinoteka')
    else:
        form = DiaryForm()
    return render(request, 'vinoteka/create_diary.html', {'form': form})
