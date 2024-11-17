from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Post


def index(request):
    # return HttpResponse("Привет! Это приложение blog.")
    #  context = {"latest_question_list": 0}
    return render(request, 'index.html')

def title(request):
    # return HttpResponse("Вы смотрите заголовки блогов %s." % question_id)
    blog_list = Post.objects.order_by("-published_date")[:5]
    context = {"blog_list": blog_list}
    
    return render(request, "list_of_blogs.html", context)


def content_blog(request, blog_id):
    # response = "Вы смотрите каждый блог по отдельности %s."
    one_blog = Post.objects.get(id = blog_id)
    context = {"one_blog": one_blog}
   
    # return HttpResponse(response % blog_id)
    return render(request, "oneblog.html", context)   


