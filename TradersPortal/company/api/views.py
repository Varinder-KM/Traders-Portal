from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from company.models import company_model as CompanyModel, watchlist_model as WatchlistModel
from company.api.serializers import CompanySerializer, WatchlistSerializer
from django.urls import reverse
from django.contrib.auth.models import User




@api_view(['GET', 'POST'])
def companies(request):   
    if request.method == 'GET':
        comps = CompanyModel.objects.all()
        serializer = CompanySerializer(comps, many=True)
        return Response(serializer.data)





@api_view(['POST'])
def add_comapny(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def search_company(request):
    if request.method == 'POST':
        c_name = request.data.get('company_name')
        cmps = CompanyModel.objects.filter(company_name=c_name)
        serializer = CompanySerializer(cmps, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_watchlist(request):
    data = {
        'user': request.user.id,  # Add user data to the incoming data
        'company_name': request.data.get('company_name'),
        'symbol': request.data.get('symbol'),
        'scripcode': request.data.get('scripcode')
    }
    serializer = WatchlistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        red_url  = reverse('index', args=[])
        return redirect(red_url)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_watchlist(request):
    try:
        watchlist = WatchlistModel.objects.filter(user=request.user)
        watchlist_serializer = WatchlistSerializer(watchlist, many=True)
        return Response(watchlist_serializer.data)
    except Exception as e:
        # Log the exception
        print(f'Error: {e}')
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
