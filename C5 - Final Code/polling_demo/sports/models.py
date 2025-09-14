from django.db import models

# Create your models here.
class Fixture(models.Model):
    team_a = models.CharField(max_length=100)
    team_b = models.CharField(max_length=100)
    score_a = models.IntegerField(default=0)
    score_b = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_a} vs {self.team_b}"    