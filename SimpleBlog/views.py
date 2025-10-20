from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .config import supabase


class DisplayPosts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data}, status=status.HTTP_200_OK)
    
class PostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        image=request.FILES["post_images"] # to specify that we are getting file
        res = supabase.storage.from_("airbnb users").upload(
            f"images/{image.name}",
            image.read(),
            {"content-type":image.content_type}
        ) # storage - shows we are storing
        #    from_(bucket name)- the file location on supabase
        #   images/{image.name} - creates a folder call images and stores the images in there by their names
        #   content-type - description of the image(optional)

        image_url=supabase.storage.from_("airbnb users").get_public_url(f"images/{image.name}")
        # get image url from supabase 
        data = request.data # get the request sent by the user
        data['post_images']=image_url # point to the image request and stores the image url there 

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            posts = Post.objects.first()
            return Response({"post": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateDeletePostView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        try:
            post=Post.objects.get(pk=id, author=request.user)
        except Post.DoesNotExist:
            return Response({"Error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)  
        serializer=PostSerializer(instance=post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"post": serializer.data}, status=status.HTTP_200_OK)
        return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            post=Post.objects.get(pk=id, author=request.user)
        except Post.DoesNotExist:
            return Response({"Error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)  
        post.delete()
        return Response({"messages": "Post deleted successfully"}, status=status.HTTP_200_OK)
            
                

