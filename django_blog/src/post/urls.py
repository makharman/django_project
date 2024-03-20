from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='list_post'),
    path('create/', views.CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail_post'),
    path('about/', views.AboutView.as_view(), name='about_post'),
    
]
