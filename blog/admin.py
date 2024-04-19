from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ("title", "slug", "author", "created_on", "status")
    search_fields = ["title"]
    list_filter = ["status"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)

# Register your models here.
admin.site.register(Comment)
