from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    topics = Post.objects.values_list('topic', flat=True).distinct()
    return render(request, 'news/home.html', {'posts': posts, 'topics': topics})



