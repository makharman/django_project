
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, TemplateView,DeleteView
from rest_framework import status
from django.views.generic.edit import CreateView
from .serializers import PostListSerializer,PostCreateSerializer,PostListModelSerializer,PostCreateModelSerializer
from .serializers import PostDeleteModelSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


from post.models import Post
from post.forms import PostForm

class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name='list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name='detail.html'
    context_object_name = 'post'    
   

class CreatePostView(CreateView):
    model = Post
    template_name='create.html'
    fields = ['title', 'user', 'status']
    
class AboutView(TemplateView):
    template_name='about.html'
     
     

@csrf_exempt
def get_post_handler(request):
    if request.method == 'POST':
        return HttpResponse('POST request')
    is_active = request.GET.get('is_active')
    user = request.GET.get('user')
    
    posts = Post.objects.filter(is_actual=bool(is_active), user__username=user).values('title')

    response = {
        'posts': list(posts)
    }   
    
    return JsonResponse(response) 



# def page_404(request, exception):
#     return HttpResponseNotFound("<h3>Page not found:^</h3>")




class PostApiView(APIView):
    def get(self, request):
        post_queryset = Post.objects.all()      
        serializer = PostListModelSerializer(post_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostCreateModelSerializer(data = request.data)
        serializer.is_valid()
        
        user = serializer.validated_data.pop('user')
        print(user,'!!!!')
        user_obj = User.objects.get(id=user.id)
        categories = serializer.validated_data.pop('categories')
        print(serializer.validated_data)
        post = Post.objects.create(user=user_obj, **serializer.validated_data)
        print(post.categories.all())
        post.categories.add(*categories)
        
        return Response('test')
    

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer = PostDeleteModelSerializer(queryset)

    def delete(self, request,*args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response('Deleted!!!')

    


# def post_archive(request, year):
#     if int(year) > 2024 or int(year) < 1995:
#         # raise Http404
#         return redirect('post_detail',3)
#     return HttpResponse(f'archive for: {year}')   


# def posts(request):
#     posts = Post.objects.all()
#     data = {
#         'posts': posts,
#     }
#     return render(request, 'posts.html', context=data)  

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'post_detail.html', {'post': post})  

# def post_archive(request, year):
#     if int(year) > 2024 or int(year) < 1995:
#         raise Http404
#     return HttpResponse(f'archive for: {year}')





