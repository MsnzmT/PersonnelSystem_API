from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutView, UserProfileView


urlpatterns = [
    path('login/', view=obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]