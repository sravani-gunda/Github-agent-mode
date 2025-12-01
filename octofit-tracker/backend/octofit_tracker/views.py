from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion
from .serializers import (
    UserSerializer, UserProfileSerializer, ActivitySerializer,
    TeamSerializer, LeaderboardEntrySerializer, WorkoutSuggestionSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('-points')
    serializer_class = LeaderboardEntrySerializer

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer
