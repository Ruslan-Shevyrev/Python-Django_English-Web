from django.shortcuts import render
from .models import Articles


def all_posts(request):
    posts = Articles.objects.order_by('-date')
    return render(request, 'posts/all_posts.html', {'posts': posts})
