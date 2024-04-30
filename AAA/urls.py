from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .api import *

urlpatterns = [
    path('login/',login , name='login'),
    path('signup/', signup, name='token_refresh'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]