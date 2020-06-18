from django.urls import path, re_path
from django.conf.urls import handler404
from . import views


app_name='blog'
urlpatterns = [
    path('', views.index, name='blog-home'),
    path('posts/<int:id>/', views.show, name='blog-post'),
    #re_path(r'posts/(?P<id>[0-9]+)$', views.show, name='blog-post')
]