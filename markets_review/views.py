from django.shortcuts import render
from django.views import generic
from .models import Market

# Create your views here.

class MarketList(generic.ListView):
    queryset = Market.objects.all()
    template_name = "market_list.html"
    
