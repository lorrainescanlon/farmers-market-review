from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Market, Review, Picture
from news.models import News
from .forms import ReviewForm
from django.conf import settings
from django.db.models import Sum, Q
from django.core.paginator import Paginator


def market_list(request):
    """Return all approved markets and approved newsletter headlines"""
    queryset = Market.objects.all().order_by('name')
    markets = queryset.filter(status=1)
    paginator = Paginator(markets, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    news = News.objects.filter(status=1)
    headlines = news.filter(newsletter=True)

    context = {
        "markets": markets,
        "headlines": headlines,
        "page_obj": page_obj
    }

    return render(request, "markets_review/index.html", context)


def search_view(request):
    """Return search results"""
    query = request.GET.get('q')
    
    object_list = Market.objects.filter(Q(name__icontains=query) | Q(location__icontains=query)).order_by('name')
    
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    news = News.objects.filter(status=1)
    headlines = news.filter(newsletter=True)

    context = {
        "query": query,
        "object_list": object_list,
        "headlines": headlines,
        "page_obj": page_obj
    }
    return render(request, "markets_review/search_results.html", context)



def market_detail(request, slug):
    """Display information for an individual market details"""

    queryset = Market.objects.filter(status=1)
    market = get_object_or_404(queryset, slug=slug)

    """display reviews associated with the market, count returned reviews"""
    reviews = market.reviews.all().order_by("-created_on")
    review_count = market.reviews.filter(approved=True).count()

    """count reviews with visit again value of yes and no"""
    visityes_count = market.reviews.filter(visit_again=True).count()
    visitno_count = market.reviews.filter(visit_again=False).count()
    
    """calculate percentage of visit again yes and no choices"""
    if review_count <= 0:
        visityes_percent = 0
        visitno_percent = 0
    else:
        visityes_percent = int((visityes_count/review_count)*100)
        visitno_percent = int((visitno_count/review_count)*100)

    """calculate review stars ratings for the market"""
    if review_count <= 0:
        market_stars = "No reviews yet"
    else:
        market_stars = int(Review.objects.filter(market=market, approved=True).aggregate(total=Sum('stars_rating'))["total"]/review_count)

    """google maps key"""
    key = settings.GMAPS_API_KEY    

    """market picture carousel"""
    pictures = Picture.objects.filter(market=market)

    review_form = ReviewForm()

    """validate new review"""
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.market = market
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval')
            review_form = ReviewForm()

    context = {
        "market": market,
        "reviews": reviews,
        "review_count": review_count,
        "visityes_percent": visityes_percent,
        "visitno_percent": visitno_percent,
        "market_stars": market_stars,
        "key": key,
        "review_form": review_form,
        "pictures": pictures,
        }

    return render(
        request, "markets_review/market_detail.html", context
    )


def review_edit(request, slug, review_id):
    """view to edit review"""
    if request.method == "POST":

        queryset = Market.objects.filter(status=1)
        market = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.market = market
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!') 

    return HttpResponseRedirect(reverse('market_detail', args=[slug]))



def review_delete(request, slug, review_id):
    """view to delete review"""

    queryset = Market.objects.filter(status=1)
    market = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete reviews that you have created!')

    return HttpResponseRedirect(reverse('market_detail', args=[slug]))
