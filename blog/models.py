from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = ((0, "draft"), (1, "published"))
# Create your models here.
class Post(models.Model):
    """
    A model representing a blog post about a wine.

    Fields:
        title (CharField): The name of the wine. Must be unique.
        slug (SlugField): The URL-friendly version of the title. Must be unique.
        author (ForeignKey): The user who authored the post. Links to Django's built-in User model.
        year (PositiveIntegerField): The year of the wine.
        shop (CharField): The shop where the wine can be bought.
        content (TextField): The description of the wine.
        LATER: image=CloudinaryFiled('image', default:'placeholder) CLOUDINARY !
        created_on (DateTimeField): The date and time when the post was created. 
        status (CharField): The status of the post. Can be either 'draft' or 'published'.
        winery (CharField): The winery that produced the wine.
        grapes (CharField): The grapes used to make the wine.

    The posts are ordered by the 'created_on' field in descending order.
    """

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    winery = models.CharField(max_length=100)
    grapes = models.CharField(max_length=200)
    region = models.CharField(max_length=200, null=True)
    year = models.PositiveIntegerField()
    shop = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)                 

# Meta Class
    class Meta:
        ordering = ["created_on"]
# Dunder Method
    def __str__(self):
        return f"{self.title} | suggested by {self.author}"

class Comment(models.Model):
    """
    A model representing a comment on a blog post.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_author"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
