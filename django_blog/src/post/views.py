import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Post


def posts(request):
    posts = Post.objects.all()
    data = {
        'posts': posts,
    }
    return render(request, 'posts.html', context=data)  

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})  

def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
        raise Http404
    return HttpResponse(f'archive for: {year}')

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



def page_404(request, exception):
    return HttpResponseNotFound("<h3>Page not found:^</h3>")




