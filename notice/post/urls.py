from django.urls import path

from . import views


app_name = "post"
urlpatterns= [
    path('',views.index, name="all_posts"),
    path('<int:msg_id>/like/', views.like, name="like"),
    path('<int:msg_id>/content/',views.content, name="content"),
    path('<int:msg_id>/text_post',views.text, name="text"),
    path('<int:msg_id>/liked', views.likepress, name="likepress" ),
    path('<int:msg_id>/comments/', views.comments, name="comments"),
    path('<int:msg_id>/comments/write', views.comment_write, name="comment_write"),
]