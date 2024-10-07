from django.contrib.auth.models import User
from django.db import models


class Breeds(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cats(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breeds, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cats')

    def __str__(self):
        return self.name


class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cats, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = (('user', 'cat'),)

    def __str__(self):
        return f'{self.user.username} rated tha cat {self.cat.name}: {self.rating}'
