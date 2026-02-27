from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Ensure unique index on email
        db.users.create_index([('email', 1)], unique=True)

        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Spider-Man', 'Captain America'])
        dc = Team.objects.create(name='dc', members=['Batman', 'Superman', 'Wonder Woman'])

        # Sample users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')

        # Sample activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-02-27')
        Activity.objects.create(user='Spider-Man', type='cycle', duration=45, date='2026-02-26')
        Activity.objects.create(user='Batman', type='swim', duration=20, date='2026-02-25')
        Activity.objects.create(user='Superman', type='fly', duration=60, date='2026-02-24')

        # Sample leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Sample workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for=['marvel', 'dc'])
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for=['marvel'])
        Workout.objects.create(name='Squats', description='Do 15 squats', suggested_for=['dc'])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
