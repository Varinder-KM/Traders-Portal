from django.urls import path
from company import views

urlpatterns = [
   path('', views.index, ),
   path('search/', views.search, name='index'),
   path('add_company/', views.add_comapny),
   path('watchlist/', views.watchlist),
]
