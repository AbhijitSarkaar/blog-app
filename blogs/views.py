from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category, Comment
from django.contrib.auth.models import User
from blog_main.forms import AddCommentForm

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    post = get_object_or_404(Blog, slug=slug, status="Published")
    comments = Comment.objects.filter(blog = post.id)
    form = AddCommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }

    return render(request, 'blogs.html', context)

def add_comment(request, post_id):
    print('add_comment view')
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            post = Blog.objects.get(pk=post_id)
            comment.blog = post
            comment.save()
            return redirect('home')
