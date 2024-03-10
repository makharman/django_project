from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.post_detail),
    re_path(r'^archieve/(?P<year>[0-9]{4})/$', views.post_archive),
    path('post/get_post/',views.get_post_handler),
    
]