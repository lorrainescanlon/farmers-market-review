from django.shortcuts import render
from django.views import generic
from .models import Market

# Create your views here.

class MarketList(generic.ListView):
    queryset = Market.objects.all().order_by('name')
    template_name = "markets_review/index.html"
    paginate_by = 6
