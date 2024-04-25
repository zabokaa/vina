from django.contrib import admin
from django.urls import path, include
from intro import views as intro_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls"), name="blog"),
    path("intro/", intro_views.age_verification, name="intro"),
    path("summernote/", include("django_summernote.urls")),
    path("vinoteka/", include("vinoteka.urls")),
    path("", intro_views.age_form, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
