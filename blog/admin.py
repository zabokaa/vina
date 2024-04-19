from django.contrib import admin
from .models import Post
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ("title", "slug", "author", "created_on", "status")
    search_fields = ["title"]
    list_filter = ["status"]
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Comment)
