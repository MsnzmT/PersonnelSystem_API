from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutView


urlpatterns = [
    path('login/', view=obtain_auth_token),
    path('logout/', LogoutView.as_view()),
]