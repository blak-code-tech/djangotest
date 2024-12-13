from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts',views.GetAllPosts,name='posts'),
    path("create-post",views.CreatePost,name="create-post"),
    path("delete-post/<int:id>",views.DeletePost,name="delete-post"),
    path("posts/<int:id>",views.GetPost,name="get-post"),
]