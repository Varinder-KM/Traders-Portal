from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

import firebase_admin
from firebase_admin import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings


def login_page(requests):
    return render(requests, 'account/login.html')


def post_login(requests):
    if requests.method == 'POST':
        username = requests.POST.get('user_name')
        password = requests.POST.get('user_password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(requests, 'Invalid Username')
            return redirect('/accounts/login')
        
        user = authenticate(username=username, password = password)

        if user is None:
            messages.error(requests, 'Invalid Paswword')
            return redirect('/accounts/login')
        
        else:
            login(requests, user)
            return redirect('/company/')






def signup_page(requests):
    return render(requests, 'account/signUp.html')


def post_signup(requests):
    if requests.method == 'POST':
        f_name = requests.POST.get('first_name')
        l_name = requests.POST.get('last_name')
        u_name = requests.POST.get('user_name')
        email = requests.POST.get('user_email')
        password = requests.POST.get('user_password')

        if User.objects.filter(username= u_name).exists():
            messages.error(requests, 'User Already Exsits')
            return redirect('/accounts/signup')
        else:
            user = User(
                first_name = f_name,
                last_name = l_name,
                username = u_name,
                email   = email
                )
            user.set_password(password)
            user.save()
            return redirect('/accounts/login')


def logout_page(request):
    logout(request)
    return redirect('/accounts/login')





# google login

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT_KEY_PATH)
    firebase_admin.initialize_app(cred)



@api_view(['POST'])
def google_login(request):
    id_token = request.data.get('idToken')
    if not id_token:
        return JsonResponse({'error': 'Missing idToken'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Verify the ID token using Firebase Admin SDK
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token['email']
        
        # Check if the user already exists in the Django database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Create a new user if not exists
            user = User.objects.create_user(username=email, email=email)
        
        # Log the user in
        login(request, user)
        
        # Return a successful response
        return JsonResponse({'uid': user.id, 'username': user.username})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)