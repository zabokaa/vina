from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm


# views

class PostList(generic.ListView):
    """
    Display a list of approved posts,
    4 posts per page. 
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 4
    

def post_detail(request, slug):
    """
    Display a single blog post (approved posts only) with comments form, 
    and comments.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form, }
    )


def comment_edit(request, slug, comment_id):
    """
    Display edit button for logged-in users' own comments and handle edit request.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Display delete button for logged-in users' own comments and handle delete request.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your comment is deleted!')
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def like_post(request, post_id):
    """
    Add or remove a post from the user's wine list (liked posts).
    """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            messages.success(request, 'You have unliked this post. '
                             'It will be removed from your Vinotheque.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post. '
                             'It will be added to your Vinotheque.')
    return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
