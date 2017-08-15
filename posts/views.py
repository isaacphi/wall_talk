from django.shortcuts import render
from django.http import HttpResponse

from .models import Tag, Post

def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    p = Post.objects.get(id=post_id)
    return HttpResponse(p.text)