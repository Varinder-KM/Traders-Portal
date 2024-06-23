from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login_page),
    path('postlogin/', views.post_login),
    path('signup/', views.signup_page),
    path('postsignup/', views.post_signup),
    path('logout/', views.logout_page),
    path('google_login/', views.google_login)
]
