from django.shortcuts import render
from .models import Posts

# Create your views here.


def index(request):
    posts = Posts.objects.all()[::-1]
    return render(request, "index.html", {"posts": posts})


def blog(request):
    posts = Posts.objects.all()[::-1]
    return render(request, "blog.html", {"posts": posts})


def post(request, link):
    posts = Posts.objects.get(title=link)
    return render(request, "post.html", {"posts": posts})
