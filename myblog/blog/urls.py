from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

     # ex: /blog/5/
    path("title/", views.title, name="title"),
    # ex: /blog/5/results/
    # path("title/<int:question_id>", views.content_blog, name="content_blog"),
    path("title/content_blog/<int:blog_id>", views.content_blog, name="content_blog")
   
]
