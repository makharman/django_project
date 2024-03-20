from django.urls import path
from api import views

urlpatterns = [
    path('post_list_apiview/', views.PostList.as_view(), name='post_list'),
    path('post_create_apiview/', views.PostCreate.as_view(), name='post_create'),
    path('post_detail_apiview/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post_delete_apiview/<int:pk>/', views.PostDeleteAPIView.as_view(), name='delete_post'),
]
