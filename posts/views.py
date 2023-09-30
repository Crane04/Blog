from django.shortcuts import render
from .models import Posts

# Create your views here.


def index(request):
    posts = Posts.objects.all()[::-1]
    context = {
        "title": "Mayowa's Portfolio",
        "posts": posts,
        "favicon":"static/assets/blog/myImage.png"
    }
    return render(request, "index.html", context)


def blog(request):
    posts = Posts.objects.all()[::-1]

    context = {
        "title": "Mayowa's Portfolio",
        "posts": posts,
        "favicon":"static/assets/blog/myImage.png"
    }
    return render(request, "blog.html", context)


def post(request, link):
    post = Posts.objects.get(title=link)
    context = {
        "title": post.title,
        "post": post,
        "favicon": "https://res.cloudinary.com/dsaddflhf/image/upload/v1/" + str(post.image_exp)
    }
    return render(request, "post.html", context)
