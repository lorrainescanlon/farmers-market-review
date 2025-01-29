from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Market
from django.conf import settings

# Create your views here.

class MarketList(generic.ListView):
    queryset = Market.objects.all().order_by('name')
    template_name = "markets_review/index.html"
    paginate_by = 6

def market_detail(request, slug):
    """
    Display information for an individual :model:`markets_review.Market`. 
    **Context**
    ``market``
        An instance of :model:`markets_review.Market`
    
    **Template**
    :template:`markets_review/market_detail.html`
    """

    queryset = Market.objects.filter(status=1)
    market = get_object_or_404(queryset, slug=slug)
    key = settings.GMAPS_API_KEY
    context = {
        "market": market,
        "key": key
    }
    

    return render(
        request,
        "markets_review/market_detail.html",
        context,
    )