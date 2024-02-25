# views.py
from django.shortcuts import render
from django.utils import timezone
from .models import AuctionItem
from .forms import AuctionSearchForm
from django.db.models import Q


def auction_items(request):
    current_time = timezone.now()

    # Live Auctions
    live_auctions = AuctionItem.objects.filter(start_time__lte=current_time, end_time__gte=current_time)

    # Upcoming Auctions
    upcoming_auctions = AuctionItem.objects.filter(start_time__gt=current_time, end_time__gt=current_time)

    return render(request, 'auction_items.html', {
        'live_auctions': live_auctions,
        'upcoming_auctions': upcoming_auctions,
    })


def search_auction(request):
    query = request.GET.get('query', '')
    auctions = AuctionItem.objects.all()
    search_results = []

    if query:
        search_results = AuctionItem.objects.filter(
            Q(title__icontains=query) | Q(address__icontains=query)
        )

    return render(request, 'auction_search.html', {'auctions': auctions, 'search_results': search_results, 'query': query})