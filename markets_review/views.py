from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Market, Review, Ratings
from .forms import ReviewForm
from django.conf import settings
from django.db.models import Sum


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
    
    ``key``
        A variable pointing to google maps api key
    
    **Template**
    :template:`markets_review/market_detail.html`
    """

    queryset = Market.objects.filter(status=1)
    market = get_object_or_404(queryset, slug=slug)
    reviews = market.reviews.all().order_by("-created_on")
    review_count = market.reviews.filter(approved=True).count()
    key = settings.GMAPS_API_KEY

    if review_count <= 0:
        market_stars = "No reviews yet"
    else:
        market_stars = Review.objects.filter(market=market, approved=True).aggregate(total=Sum('stars_rating'))["total"]/review_count

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.market = market
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
    )

    review_form = ReviewForm()

    context =  {
            "market": market,
            "reviews": reviews,
            "review_count": review_count,
            "market_stars": market_stars,
            "key": key,
            "review_form": review_form,
        }

    return render(
        request, "markets_review/market_detail.html", context
    )