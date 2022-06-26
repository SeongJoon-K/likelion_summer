from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.

from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

# 포스트 리스트 뷰
@api_view(['GET'])
def ListPost(request):
    # GET 방식을 받아왔을 때
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data)

