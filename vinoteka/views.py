from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import View
from blog.models import Post
from .models import Diary
from .forms import DiaryForm


def diary_list(request):
    """"
    Display list of all diary entries created by the currently logged-in user.
    """
    diaries = Diary.objects.filter(user=request.user)
    return render(request, 'vinoteka/diary_list.html', {'diaries': diaries})


@login_required
def liked_posts(request):
    """"
    Display list of posts liked by the currently logged-in user.
    """
    posts = Post.objects.filter(likes=request.user)
    form = DiaryForm()
    diaries = Diary.objects.filter(user=request.user)
    return render(
        request,
        'vinoteka/liked_posts.html',
        {'posts': posts, 'form': form, 'diaries': diaries}
        )


@login_required
def create_diary(request):
    """
    Displays form for creating a new diary entry
    and handle POST request to save the new entry
    for the currently logged-in user.
    """
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your diary entry has been added!'
                )
            print(form.errors)
            return redirect('vinoteka')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error in your entry. Please try again.')
    else:
        form = DiaryForm()
    return render(
        request,
        'vinoteka/create_diary.html',
        {'form': form}
        )


@login_required
def diary_detail(request, pk):
    """
    Display details of a specific diary entry.
    Only working for a diary entry that belongs
    to the currently logged-in user.
    """
    diary = get_object_or_404(Diary, pk=pk, user=request.user)
    return render(
        request,
        'vinoteka/diary_detail.html',
        {'diary': diary}
        )


class DiaryDeleteView(View):
    def post(self, request, pk):
        diary = get_object_or_404(Diary, pk=pk)
        if diary.user == request.user:
            diary.delete()
            messages.add_message(
                request, messages.SUCCESS,
                'Your diary entry has been deleted!'
                )
        return redirect(reverse('vinoteka'))
