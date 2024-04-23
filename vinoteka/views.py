from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog.models import Post
from .models import Diary


@login_required
def liked_posts(request):
    posts = Post.objects.filter(likes=request.user)
    return render(request, 'vinoteka/liked_posts.html', {'posts': posts})


@login_required