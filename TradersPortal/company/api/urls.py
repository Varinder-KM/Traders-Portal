from django.urls import path
from company.api import views

urlpatterns = [
    path('add_company/', views.add_comapny, name='add_comapny'),
    path('companies/', views.companies, name='company_list'),
    path('search_company/', views.search_company, name='company'),
    path('watchlists/', views.get_watchlist, name='get_watchlist'),
    path('add_to_watchlist/<int:company_id>/', views.add_to_watchlist, name='add_to_watchlist'),
]
