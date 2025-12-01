from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'avatar']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'calories_burned', 'date']

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'members']

class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'points']

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'suggestion', 'created_at']
