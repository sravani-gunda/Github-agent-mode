"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .views import (
    UserViewSet, UserProfileViewSet, ActivityViewSet,
    TeamViewSet, LeaderboardEntryViewSet, WorkoutSuggestionViewSet
)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('/api/users/'),
        'userprofiles': request.build_absolute_uri('/api/userprofiles/'),
        'activities': request.build_absolute_uri('/api/activities/'),
        'teams': request.build_absolute_uri('/api/teams/'),
        'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
        'workoutsuggestions': request.build_absolute_uri('/api/workoutsuggestions/'),
    }, status=status.HTTP_200_OK)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)
router.register(r'workoutsuggestions', WorkoutSuggestionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api_root'),
]
