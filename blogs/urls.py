from django.urls import path
from . import views 

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('add/<int:post_id>/', views.add_comment, name='add_comment')
]