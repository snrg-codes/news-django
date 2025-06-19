from django.shortcuts import render, get_object_or_404
from .models import Post, Topic
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    # topics = Topic.objects.values_list('slug', flat=True).distinct()
    topics = Topic.objects.all()

    return render(request, 'news/home.html', {  'posts': posts, 
                                                'topics': topics})

def filtr_po_temam(request, nazvaniye_temi):
    topic = get_object_or_404(Topic, slug=nazvaniye_temi)
    posts = topic.post_set.all().order_by('-created_at')
    topics = Topic.objects.all()
    return render(request, 'news/home.html', {  'posts': posts, 
                                                'topics': topics, 
                                                'nazvaniye_temi': nazvaniye_temi})

def otkrit_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    topics = Topic.objects.all()

    return render(request, 'news/post.html', {  'post': post, 
                                                'topics': topics})
                                                
