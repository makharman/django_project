from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserAccount
from post.models import Post
from .serializers import PostListSerializer
from rest_framework import status


class AccountAPIView(APIView):
    def get(self, request):
        account_mobile_phones = UserAccount.objects.all().values('mobile_phone')
        print(request.parsers)
        return Response(list(account_mobile_phones))

    def post(self, request):
        print(request.data)
        return Response('test')



    
    

class PostDeleteAPIView(APIView):
    def delete(self, request):
        if Post.objects.exists():
            post_delete = Post.objects.first()
            post_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

