from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    print(request.GET)
    print(request.headers)
    return HttpResponse('index')

def post_detail(request, post_id):
    return HttpResponse(f'detail: {post_id}')

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




