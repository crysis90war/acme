from django.shortcuts import render
from .mocks import Post


def index(request):
    posts = Post.all()
    return render(request, 'blog/index.html', {'posts': posts, 'title': 'Homepage'})


def show(request, id):
    post = Post.find(id)
    return render(request, 'blog/show.html', {'post': post, 'title': 'Post {}'.format(id)})
