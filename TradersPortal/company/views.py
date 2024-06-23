from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from company.models import company_model, watchlist_model
import requests
from django.conf import settings


def add_comapny(request):
    return render(request, 'company/add_company.html')


def index(request):
    response = requests.get(f'{settings.API_BASE_URL}/companies/')
    companies = response.json() if response.status_code == 200 else []
    context = {'comp': companies}
    return render(request, 'company/index.html', context)


def search(request):
    if request.method == 'POST':
        data = {'company_name': request.POST.get('company_name')}
        response = requests.post(f'{settings.API_BASE_URL}/search_company/', data=data)
        print(response)
        companies = response.json() if response.status_code == 200 else []
        context = {'comp': companies}
        return render(request, 'company/index.html', context)



def watchlist(request):
    response = requests.get(f'{settings.API_BASE_URL}/watchlists/')
    companies = response.json() if response.status_code == 200 else []
    context = {'comp': companies}
    print(context)
    return render(request, 'company/watchlist.html', context)