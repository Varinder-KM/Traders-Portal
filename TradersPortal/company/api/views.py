from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from company.models import company_model as CompanyModel, watchlist_model as WatchlistModel
from company.api.serializers import CompanySerializer, WatchlistSerializer
from django.urls import reverse





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
        red_url  = reverse('index', args=[])
        return redirect(red_url)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def search_company(request):
    if request.method == 'POST':
        c_name = request.POST.get('company_name')
        cmps = CompanyModel.objects.filter(company_name=c_name)
        serializer = CompanySerializer(cmps, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_watchlist(request, company_id):
    company_instance = get_object_or_404(CompanyModel, pk=company_id)
    watchlist, created = WatchlistModel.objects.get_or_create(user=request.user, company=company_instance)
    if created:
        red_url  = reverse('index', args=[])
        return redirect(red_url)
    else:
        return Response({'status': 'Company already in watchlist'}, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_watchlist(request):
    watchlist = WatchlistModel.objects.filter(user=request.user)
    serializer = WatchlistSerializer(watchlist, many=True)
    return Response(serializer.data)
