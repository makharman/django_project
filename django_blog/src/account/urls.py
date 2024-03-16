from django.urls import path
from . import views
from .views import PostDeleteAPIView 

urlpatterns = [
    path('', views.AccountAPIView.as_view(), name='account'),
    path('post/', views.PostAPIView.as_view(), name='post'),
    path('post/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
]

