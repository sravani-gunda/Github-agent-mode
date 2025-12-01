from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        WorkoutSuggestion.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()

        # Superheroes
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'bio': 'Genius billionaire', 'avatar': 'http://example.com/ironman.png'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'bio': 'Super soldier', 'avatar': 'http://example.com/cap.png'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'bio': 'Friendly neighborhood', 'avatar': 'http://example.com/spiderman.png'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'bio': 'Dark knight', 'avatar': 'http://example.com/batman.png'},
            {'username': 'superman', 'email': 'superman@dc.com', 'bio': 'Man of steel', 'avatar': 'http://example.com/superman.png'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'bio': 'Amazon princess', 'avatar': 'http://example.com/wonderwoman.png'},
        ]

        marvel_users = []
        dc_users = []
        for hero in marvel_heroes:
            user = User.objects.create(username=hero['username'], email=hero['email'])
            UserProfile.objects.create(user=user, bio=hero['bio'], avatar=hero['avatar'])
            marvel_users.append(user)
        for hero in dc_heroes:
            user = User.objects.create(username=hero['username'], email=hero['email'])
            UserProfile.objects.create(user=user, bio=hero['bio'], avatar=hero['avatar'])
            dc_users.append(user)

        # Teams
        marvel_team = Team.objects.create(name='Marvel')
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='DC')
        dc_team.members.set(dc_users)

        # Activities
        Activity.objects.create(user=marvel_users[0], activity_type='Flying', duration=60, calories_burned=500, date='2025-12-01')
        Activity.objects.create(user=marvel_users[1], activity_type='Shield Training', duration=45, calories_burned=350, date='2025-12-01')
        Activity.objects.create(user=marvel_users[2], activity_type='Web Swinging', duration=30, calories_burned=250, date='2025-12-01')
        Activity.objects.create(user=dc_users[0], activity_type='Martial Arts', duration=50, calories_burned=400, date='2025-12-01')
        Activity.objects.create(user=dc_users[1], activity_type='Flight', duration=70, calories_burned=600, date='2025-12-01')
        Activity.objects.create(user=dc_users[2], activity_type='Lasso Training', duration=40, calories_burned=300, date='2025-12-01')

        # Leaderboard
        LeaderboardEntry.objects.create(user=marvel_users[0], points=200)
        LeaderboardEntry.objects.create(user=marvel_users[1], points=180)
        LeaderboardEntry.objects.create(user=marvel_users[2], points=160)
        LeaderboardEntry.objects.create(user=dc_users[0], points=210)
        LeaderboardEntry.objects.create(user=dc_users[1], points=190)
        LeaderboardEntry.objects.create(user=dc_users[2], points=170)

        # Workout suggestions
        WorkoutSuggestion.objects.create(user=marvel_users[0], suggestion='Try arc reactor sprints')
        WorkoutSuggestion.objects.create(user=dc_users[0], suggestion='Practice rooftop jumps')

        self.stdout.write(self.style.SUCCESS('Superhero test data populated successfully.'))