from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Market, Review, Ratings, Picture
from .forms import ReviewForm
from django.conf import settings
from django.db.models import Sum, Q


# Create your views here.


class MarketList(generic.ListView):
    """Display all markets in paginated form"""

    queryset = Market.objects.all().order_by('name')
    template_name = "markets_review/index.html"
    paginate_by = 6



class SearchView(generic.ListView):
    """Display search results in paginated form"""

    model = Market
    template_name = "markets_review/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Market.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )

        return object_list



def market_detail(request, slug):
    """Display information for an individual market"""

    queryset = Market.objects.filter(status=1)
    market = get_object_or_404(queryset, slug=slug)

    #reviews associated with the market
    reviews = market.reviews.all().order_by("-created_on")

    #count approved market reviews
    review_count = market.reviews.filter(approved=True).count()

    #count reviews who chose yes to visit again
    visityes_count = market.reviews.filter(visit_again=True).count()

    ##count reviews who chose no to visit again
    visitno_count = market.reviews.filter(visit_again=False).count()
    
    #get the percentage of yes and no choices
    if review_count <= 0:
        visityes_percent = 0
        visitno_percent = 0
    else:
        visityes_percent = int((visityes_count/review_count)*100)
        visitno_percent = int((visitno_count/review_count)*100)

    #get a total of review stars ratings for the market
    if review_count <= 0:
        market_stars = "No reviews yet"
    else:
        market_stars = int(Review.objects.filter(market=market, approved=True).aggregate(total=Sum('stars_rating'))["total"]/review_count)

    #google maps key
    key = settings.GMAPS_API_KEY    

    #market pictures to display in image carousel
    pictures = Picture.objects.filter(market=market)

    #validate new review
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
    """
    view to delete review
    """

    queryset = Market.objects.filter(status=1)
    market = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete reviews that you have created!')

    return HttpResponseRedirect(reverse('market_detail', args=[slug]))
