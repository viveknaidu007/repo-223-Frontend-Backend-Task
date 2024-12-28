from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.db.models import Prefetch
from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 10  # we can adjust to change how many posts per page

class PostListView(APIView):
    pagination_class = PostPagination

    def get(self, request, *args, **kwargs):
        # prefetch comments and limit them to the latest 3 per post
        posts = Post.objects.prefetch_related(
            Prefetch('comments', queryset=Post.comments.all().order_by('-timestamp')[:3])
        ).order_by('-timestamp')

        # paginate the posts
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(posts, request)
        
        # serialize the posts and return the response
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
