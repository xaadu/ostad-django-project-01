# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('otp-verify/', views.otp_verify_view, name='otp_verify'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),  # Added logout URL
    path('profile-update/', views.profile_update_view, name='profile_update'),  # Added profile update URL

]