from django.shortcuts import render
from django.views import Generic 
from .models import Post 

class PostList(generic.Listview):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    
