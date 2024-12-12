from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts',views.GetAllPosts,name='posts'),
    path("create-post",views.CreatePost,name="create-post"),
    path("delete-post",views.DeletePost,name="delete-post"),
    path("post",views.GetPost,name="post"),
]