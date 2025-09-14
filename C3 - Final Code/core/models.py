from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    books = models.ManyToManyField("Book", related_name='users')


class Book(models.Model):
    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction'
        NON_FICTION = 'Non-Fiction'
        MYSTERY = 'Mystery'

    name = models.CharField(max_length=128)
    genre = models.CharField(max_length=24, choices=GenreChoices.choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)  # reverse order - DESC

    def __str__(self):
        return self.name