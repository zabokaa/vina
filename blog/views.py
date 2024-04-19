from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here:
def showblog(request):
    return HttpResponse("you are seeing the blog entries now !")

# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.all()
#     template_name = "post_list.html"
#     paginate_by = 9
