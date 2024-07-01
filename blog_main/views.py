from django.shortcuts import render, redirect
from blogs.models import Blog, About, SocialLink
from .forms import RegistrationForm

def home(request):

    featured_posts = Blog.objects.filter(is_featured = True, status = 'Published')

    posts = Blog.objects.filter(is_featured = False, status = 'Published')

    about = About.objects.all()

    social_links = SocialLink.objects.all()
    
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        'social_links': social_links
    }
    return render(request, 'home.html', context)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()

    print(form)

    context = {
        'form': form
    }
    return render(request, 'register.html', context)