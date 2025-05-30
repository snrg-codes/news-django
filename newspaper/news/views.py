from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    topics = Post.objects.values_list('topic', flat=True).distinct()
    return render(request, 'news/home.html', {'posts': posts, 'topics': topics})


def filtr_po_temam(request, nazvaniye_temi):
    posts = Post.objects.filter(topic=nazvaniye_temi).order_by('-created_at')
    topics = Post.objects.values_list('topic', flat=True).distinct()
    return render(request, 'news/home.html', {'posts': posts, 'topics': topics, 'nazvaniye_temi': nazvaniye_temi})



