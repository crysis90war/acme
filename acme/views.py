from django.shortcuts import render
from django.views.defaults import page_not_found


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'pages/contact.html', {'title': 'Contact'})


def handler404(request, exception=None):
    return render(request, 'errors/404.html', {'error': exception}, status=404)


def handler500(request, exception=None):
    return render(request, 'errors/500.html', {'error': exception}, status=500)
