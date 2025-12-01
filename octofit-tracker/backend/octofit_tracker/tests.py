from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

class UserProfileTest(TestCase):
    def test_create_user_profile(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        profile = UserProfile.objects.create(user=user, bio='Test bio', avatar='http://example.com/avatar.png')
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, 'Test bio')

class ActivityTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser')
        activity = Activity.objects.create(user=user, activity_type='Running', duration=30, calories_burned=300, date='2025-12-01')
        self.assertEqual(activity.activity_type, 'Running')
        self.assertEqual(activity.duration, 30)

class TeamTest(TestCase):
    def test_create_team(self):
        user1 = User.objects.create(username='teamuser1')
        user2 = User.objects.create(username='teamuser2')
        team = Team.objects.create(name='Alpha Team')
        team.members.set([user1, user2])
        self.assertEqual(team.name, 'Alpha Team')
        self.assertEqual(team.members.count(), 2)

class LeaderboardEntryTest(TestCase):
    def test_leaderboard_entry(self):
        user = User.objects.create(username='leaderuser')
        entry = LeaderboardEntry.objects.create(user=user, points=100)
        self.assertEqual(entry.points, 100)

class WorkoutSuggestionTest(TestCase):
    def test_workout_suggestion(self):
        user = User.objects.create(username='suggestuser')
        suggestion = WorkoutSuggestion.objects.create(user=user, suggestion='Try HIIT')
        self.assertEqual(suggestion.suggestion, 'Try HIIT')
