from .models import Comment
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentSerializer

# Create your views here.

class PostCommentAPIView(APIView):
    def get(self, _, pk):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
