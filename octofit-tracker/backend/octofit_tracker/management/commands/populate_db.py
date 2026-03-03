from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        u1 = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        u2 = User.objects.create(name='Thor', email='thor@marvel.com', team='marvel')
        u3 = User.objects.create(name='Superman', email='superman@dc.com', team='dc')
        u4 = User.objects.create(name='Batman', email='batman@dc.com', team='dc')

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user='Thor', type='swim', duration=45, date='2023-01-02')
        Activity.objects.create(user='Superman', type='fly', duration=60, date='2023-01-03')
        Activity.objects.create(user='Batman', type='cycle', duration=25, date='2023-01-04')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=200)
        Leaderboard.objects.create(team='dc', points=180)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Sprints', description='Run 5 sprints', difficulty='medium')
        Workout.objects.create(name='Deadlift', description='Lift heavy weights', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
