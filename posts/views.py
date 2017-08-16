from django.shortcuts import render
from django.http import HttpResponse

from .models import Tag, Post

def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id)
    }
    return render(request, 'posts/detail.html', context)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    post.text = request.POST['edit']
    post.save()
    return detail(request, post_id)