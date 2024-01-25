# appname/urls.py
from django.urls import path
from .views import UserProfileView, UserRegistrationView, AllUserProfilesView

urlpatterns = [
    path('api/userprofile/', UserProfileView.as_view(), name='user-profile'),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
]

