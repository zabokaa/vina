from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from .models import Diary
from .forms import DiaryForm



def diary_list(request):
    diaries = Diary.objects.filter(user=request.user)
    return render(request, 'vinoteka/diary_list.html', {'diaries': diaries})

@login_required
def liked_posts(request):
    """"
    Display list of posts liked by the currently logged-in user.
    """
    posts = Post.objects.filter(likes=request.user)
    form = DiaryForm()  # create a DiaryForm instance and add form to the context
    diaries = Diary.objects.filter(user=request.user)
    return render(request, 'vinoteka/liked_posts.html', {'posts': posts, 'form': form, 'diaries': diaries})


@login_required
def create_diary(request):
    """
    Displays form for creating a new diary entry
    and handle POST request to save the new entry for the currently logged-in user.
    """
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

@login_required
def diary_detail(request, pk):
    """
    Display details of a specific diary entry.
    Only working for a diary entry that belongs to the currently logged-in user.
    """
    diary = get_object_or_404(Diary, pk=pk, user=request.user)
    return render(
        request, 
        'vinoteka/diary_detail.html', 
        {'diary': diary}
    )
