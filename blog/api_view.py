from .serializers import PostSerializer
from .models import Post 
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts,many=True, context={"request":request}).data
    return Response({"posts":data})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request,id):
    post = get_object_or_404(Post,id=id)
    data = PostSerializer(post, context={"request":request}).data
    return Response({"post":data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_search_api(request,query):
    post = Post.objects.filter(
        Q(title__icontains = query) |
        Q(description__icontains = query)
        
    )
    data = PostSerializer(post,many=True, context={"request":request}).data
    return Response({"posts":data})