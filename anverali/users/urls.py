from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('', RedirectView.as_view(url='profile')),
    path('auth/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('auth/signup/customer/', views.CustomerSignUp.as_view(), name='customer_signup'),
    path('auth/signup/freelancer/', views.FreelancerSignUp.as_view(), name='freelancer_signup'),
    path('profile/<str:username>', views.users_profile, name = 'users_profile'),  
    path('profile/', views.my_profile, name = 'profile'),  
    path('auth/logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
] 