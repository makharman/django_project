from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

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

def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    return HttpResponse('GET request')



def page_404(request, exception):
    return HttpResponseNotFound("<h3>Page not found:^</h3>")




