from django.urls import path
from company import views

urlpatterns = [
   path('', views.index, name='index'),
   path('search/', views.search),
   path('add_company/', views.add_comapny),
   path('watchlist/', views.watchlist),
]
