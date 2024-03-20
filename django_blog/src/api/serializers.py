from rest_framework import serializers
from .models import Post

class PostListSerializer(serializers.Serializer):
    title = serializers.CharField()
    status = serializers.CharField()

class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    status = serializers.CharField()
    user = serializers.IntegerField()
    categories = serializers.ListField()

class PostListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'status')
        

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','status')
        
        
class PostCreateModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title','text', 'status', 'user', 'categories')
        
class PostDeleteModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('title','text', 'status', 'user', 'categories')
