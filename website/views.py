# views.py
from django.shortcuts import render
from django.utils import timezone
from .models import AuctionItem
from .forms import AuctionSearchForm


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


def auction_search(request):
    form = AuctionSearchForm(request.GET)
    auctions = AuctionItem.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        auctions = auctions.filter(models.Q(title__icontains=search_query) | models.Q(address__icontains=search_query))

    return render(request, 'auction_search.html', {'form': form, 'auctions': auctions})