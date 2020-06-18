from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import Http404


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts, 'title': 'Homepage'})


def show(request, id):
    post = get_object_or_404(Post, pk=id)  # Post.objects.filter(pk=id).first()
    # try:
    #     post = get_object_or_404(Post, pk=id)#Post.objects.filter(pk=id).first()
    # except Post.DoesNotExist:
    #     raise get_object_or_404('Sorry the post #{} was not found'.format(id))
    return render(request, 'blog/show.html', {'post': post, 'title': 'Post {}'.format(id)})
