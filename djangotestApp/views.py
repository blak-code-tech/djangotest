from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def index(request):
    return Response({
        'status': 'success',
        'message': 'Hello World'
    })

@api_view(['GET'])
def GetAllPosts(request):
    getPosts = Post.objects.all()
    serializer = PostSerializer(getPosts,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreatePost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 201,'data': serializer.data,'message': 'Post Created Successfully'})
    else:
        return Response({
            'status': 400,
            'data': serializer.errors,
            'message': 'Post Creation Failed'
        })
        
@api_view(['DELETE'])
def DeletePost(request):
    try:
        id = request.data['id']
        Post.objects.get(id=id).delete()
        return Response({'status': 200,'message': 'Post Deleted Successfully'})
    except Post.DoesNotExist:
        return Response({'status': 404,'message': 'Post Not Found'})
    
@api_view(["GET"])
def GetPost(request):
    try:
        id = request.data['id']
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return Response({
            "data": serializer.data,
            "status": 200
        })
    except Post.DoesNotExist:
        return Response({'status': 404,'message': 'Post Not Found'})
    
@api_view(["PUT"])
def UpdatePost(request):
    try:
        id = request.data['id']
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "status": 200
            })
        else:
            return Response({
                "data": serializer.errors,
                "status": 400
            })
    except Post.DoesNotExist:
        return Response({'status': 404,'message': 'Post Not Found'})