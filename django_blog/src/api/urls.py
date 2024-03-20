from django.urls import path
from api import views

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', views.PostDeleteAPIView.as_view(), name='delete_post'),
]
