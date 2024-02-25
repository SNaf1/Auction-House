from django.urls import path
from . import views

urlpatterns = [
    path('auction-items/', views.auction_items, name='auction_items'),
    path('search-auction/', views.search_auction, name='search_auction'),
]