from django.db import models
from django.contrib.auth.models import User
# my models

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    like = models.ManyToManyField(User, related_name='likes_set')
    class Meta:
        db_table = 'question'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    class Meta:
        db_table='answer'
    
