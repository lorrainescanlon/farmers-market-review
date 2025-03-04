from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def news(request):
    
    return render( request, "news/news.html",)