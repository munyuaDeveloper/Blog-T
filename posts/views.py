from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts


# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]  # this is to limit the number of posts
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def details(request, post_id):  # This view takes the post_id and gets the details of the single post
    post = Posts.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)
