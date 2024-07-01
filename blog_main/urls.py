from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings
from blogs import views as blogs_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('<slug:slug>', blogs_views.blogs, name='blogs')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
