from django.shortcuts import render, get_object_or_404, redirect
from .models import UserMeta, Category, Post

# Create your views here.
def homepage(request):
    ctx = {
        "current_user": UserMeta.objects.get(id=1),
        "items": Post.objects.all()
    }
    return render(request, 'index.html', context=ctx)

def about(request):
    user = UserMeta.objects.get(id=1)
    ctx = {
        "current_user": user
    }
    return render(request, 'about.html', context=ctx)

def archive(request):
    ctx = {
        "count": len(Post.objects.all()),
        "code": Post.objects.filter(category__name="Code").all(),
        "design": Post.objects.filter(category__name="Design").all(),
        "photo": Post.objects.filter(category__name="Photo").all()
    }

    return render(request, 'archive.html', context=ctx)

def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.external_link:
        return redirect('/')

    context = {
        "post": post
    }

    return render(request, 'post.html', context)
