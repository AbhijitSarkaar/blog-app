from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostForm, UserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'category_count': category_count,
        'blog_count': blog_count
    }
    return render(request, 'dashboard/dashboard.html', context)


def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)



def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('categories')



def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            
            return redirect('posts')
            
    else:
        form = BlogPostForm()
    
    context = {
        'form': form
    }

    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    post = Blog.objects.get(pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data('title')
            post.slug = slugify(title) + '-' + pk 
            return redirect('posts')
    else:
        form = BlogPostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    post = Blog.objects.get(pk=pk)
    post.delete()
    return redirect('posts')


def users(request):
    users = User.objects.all()
    context = {
        'users': users 
    }
    return render(request, 'dashboard/users.html', context)


def add_user(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()

    context = {
        'form': form 
    }

    return render(request, 'dashboard/add_user.html', context)


def edit_user(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':    
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')

    else:
        form = EditUserForm(instance=user)

    context = {
        'form': form,
        'user': user 
    }

    return render(request, 'dashboard/edit_user.html', context)


def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()

    return redirect('users')

