from django.contrib import admin
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(LeaderboardEntry)
admin.site.register(WorkoutSuggestion)
