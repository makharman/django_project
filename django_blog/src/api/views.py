
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from .serializers import PostDeleteModelSerializer
from rest_framework.response import Response
from .serializers import PostListModelSerializer,PostCreateModelSerializer,PostDetailSerializer
from rest_framework.generics import CreateAPIView,ListAPIView, RetrieveUpdateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import JSONRenderer
from post.models import Post


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    
class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateModelSerializer
    permission_classes = [IsAuthenticated]
   
    

    

class PostDetail(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer  
    permission_classes = [IsAuthenticated] 
    
    
    
class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer = PostDeleteModelSerializer
    # permission_classes = [IsAuthenticated] 
    
    
    
    
    
    
    
    


# class PostApiView(APIView):
#     def get(self, request):
#         post_queryset = Post.objects.all()      
#         serializer = PostListModelSerializer(post_queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostCreateModelSerializer(data = request.data)
#         serializer.is_valid()
        
#         user = serializer.validated_data.pop('user')
#         print(user,'!!!!')
#         user_obj = User.objects.get(id=user.id)
#         categories = serializer.validated_data.pop('categories')
#         print(serializer.validated_data)
#         post = Post.objects.create(user=user_obj, **serializer.validated_data)
#         print(post.categories.all())
#         post.categories.add(*categories)
        
#         return Response('test')
    

# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer = PostDeleteModelSerializer

#     def delete(self, request,*args, **kwargs):
#         post = self.get_object()
#         post.delete()
#         return Response('Deleted!!!')   