from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member1')
        team = Team.objects.create(name='TeamA')
        team.members.add(user)
        self.assertEqual(team.name, 'TeamA')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activeuser')
        activity = Activity.objects.create(user=user, type='run', duration=30, calories=300)
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workoutuser')
        workout = Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session', date='2023-01-01')
        self.assertEqual(workout.name, 'Morning Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='TeamB')
        leaderboard = Leaderboard.objects.create(team=team, total_calories=1000, total_duration=120)
        self.assertEqual(leaderboard.total_calories, 1000)
