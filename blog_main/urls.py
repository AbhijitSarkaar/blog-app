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
    path('blogs/<slug:slug>', blogs_views.blogs, name='blogs'),
    path('comment/', include('blogs.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #dashboard
    path('dashboard/', include('dashboards.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
