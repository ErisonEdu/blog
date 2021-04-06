from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .serializers import PostlistSerializer
from .models import Post

class post_list_APIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostlistSerializer

# class post_detail_view(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostlistSerializer

def post_list(request):
    posts = Post.published.all()
    return render(request,
                'blog/post/list.html',
                {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
                            
    return render(request,
                'blog/post/detail.html',
                {'post': post})