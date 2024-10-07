from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from cats.models import Breeds, Cats, Ratings


class Command(BaseCommand):
    help = 'Create initial data for Breeds, Cats, and Ratings'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass'
        )
        self.stdout.write(self.style.SUCCESS(f'Superuser created: {superuser.username}'))

        user1 = User.objects.create_user(
            username='ordinary_user1',
            email='user1@example.com',
            password='password1'
        )
        user2 = User.objects.create_user(
            username='ordinary_user2',
            email='user2@example.com',
            password='password2'
        )
        self.stdout.write(self.style.SUCCESS(f'Ordinary users created: {user1.username} and {user2.username}'))

        breed1 = Breeds.objects.create(name='Siamese')
        breed2 = Breeds.objects.create(name='Persian')
        self.stdout.write(self.style.SUCCESS(f'Breeds created: {breed1.name} and {breed2.name}'))

        cat1 = Cats.objects.create(name='Whiskers', age=3, breed=breed1, color='Gray',
                                   description='A friendly Siamese cat.', user=user1)
        cat2 = Cats.objects.create(name='Fluffy', age=5, breed=breed2, color='White',
                                   description='A fluffy Persian cat.', user=user2)
        self.stdout.write(self.style.SUCCESS(f'Cats created: {cat1.name} and {cat2.name}'))

        Ratings.objects.create(user=user1, cat=cat1, rating=5)
        Ratings.objects.create(user=user2, cat=cat2, rating=4)
        self.stdout.write(self.style.SUCCESS('Ratings created for cats.'))
