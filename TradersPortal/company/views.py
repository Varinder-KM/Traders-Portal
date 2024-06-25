from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from company.models import company_model, watchlist_model
import requests
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token


@login_required
def add_comapny(request):
    if request.method == 'GET':
        return render(request, 'company/add_company.html')
    
    if request.method == 'POST':
        dt = request.POST
        resp = requests.post(f'{settings.API_BASE_URL}/add_company/', data=dt)
        print(resp)
        if resp.status_code == 200:
            rev_url = reverse('index', args=[])
            return redirect(rev_url)
        else:
            return HttpResponse('Something went wrong!!!!')


def index(request):
    response = requests.get(f'{settings.API_BASE_URL}/companies/')
    companies = response.json() if response.status_code == 200 else []
    context = {'comp': companies}
    return render(request, 'company/index.html', context)

@login_required
def search(request):
    if request.method == 'POST':
        data = {'company_name': request.POST.get('company_name')}
        response = requests.post(f'{settings.API_BASE_URL}/search_company/', data=data)
        print(response)
        companies = response.json() if response.status_code == 200 else []
        context = {'comp': companies}
        return render(request, 'company/index.html', context)


@login_required
def watchlist(request):
    session = requests.Session()
    session.cookies.update(request.COOKIES)  # Pass session cookies

    csrf_token = get_token(request)
    headers = {'X-CSRFToken': csrf_token}

    try:
        response = session.get(f'{settings.API_BASE_URL}/watchlists/', headers=headers)
        if response.status_code == 200:
            companies = response.json()
        else:
            logger.error(f'Failed to fetch watchlist: {response.status_code}')
            companies = []
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        companies = []

    context = {'comp': companies}
    return render(request, 'company/watchlist.html', context)