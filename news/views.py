from django.shortcuts import render
from .models import News


def news_letter(request):
    """
    A view to return news items
    """

    news = News.objects.filter(status=1)
    articles = news.filter(newsletter=True)

    context = {
        "news": news,
        "articles": articles,
    }

    return render(request, "news/news.html", context)
