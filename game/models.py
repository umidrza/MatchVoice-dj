from django.db import models
from django.contrib.auth.models import User


class WordSet(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wordsets')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name    


class Word(models.Model):
    term = models.CharField(max_length=20)
    definition = models.CharField(max_length=100)
    wordset = models.ForeignKey(WordSet, on_delete=models.CASCADE, related_name='words')

    def __str__(self):
        return self.term
    

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    wordset = models.ForeignKey(WordSet, on_delete=models.CASCADE, related_name='scores')
    seconds = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} | {self.seconds}"
    

