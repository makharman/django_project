from rest_framework import serializers
from .models import Post



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
        fields = ('title','text', 'status','image', 'user', 'categories')
    

        
class PostDeleteModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('title','text', 'status', 'user', 'categories')
        
    def validate_title(self, title):
        
        if not title:
            raise serializers.ValidationError("Title cannot be empty")
        return title
