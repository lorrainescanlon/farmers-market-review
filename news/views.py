from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import News

# Create your views here.


class NewsLetter(generic.ListView):

    model = News
    template_name = "news/news.html"

    def get_queryset(self):
        object_list = News.objects.all()

        print(object_list)
        print("Hello")

        return object_list
    

def news_letter(request):

    news = News.objects.filter(status=1)
    articles = news.filter(newsletter=True)

    context = {
        "news": news,
        "articles": articles,
    }

    return render(request, "news/news.html", context)