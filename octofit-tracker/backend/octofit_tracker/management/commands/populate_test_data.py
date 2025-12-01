from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate octofit_db with test data'

    def handle(self, *args, **kwargs):
        # Create users
        user1 = User.objects.create(username='alice', email='alice@example.com')
        user2 = User.objects.create(username='bob', email='bob@example.com')
        user3 = User.objects.create(username='carol', email='carol@example.com')

        # Create profiles
        UserProfile.objects.create(user=user1, bio='Runner', avatar='http://example.com/alice.png')
        UserProfile.objects.create(user=user2, bio='Cyclist', avatar='http://example.com/bob.png')
        UserProfile.objects.create(user=user3, bio='Swimmer', avatar='http://example.com/carol.png')

        # Create activities
        Activity.objects.create(user=user1, activity_type='Running', duration=45, calories_burned=400, date='2025-12-01')
        Activity.objects.create(user=user2, activity_type='Cycling', duration=60, calories_burned=600, date='2025-12-01')
        Activity.objects.create(user=user3, activity_type='Swimming', duration=30, calories_burned=250, date='2025-12-01')

        # Create team
        team = Team.objects.create(name='OctoFit Champs')
        team.members.set([user1, user2, user3])

        # Leaderboard
        LeaderboardEntry.objects.create(user=user1, points=120)
        LeaderboardEntry.objects.create(user=user2, points=150)
        LeaderboardEntry.objects.create(user=user3, points=100)

        # Workout suggestions
        WorkoutSuggestion.objects.create(user=user1, suggestion='Try interval running')
        WorkoutSuggestion.objects.create(user=user2, suggestion='Increase cycling resistance')
        WorkoutSuggestion.objects.create(user=user3, suggestion='Add butterfly stroke')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
