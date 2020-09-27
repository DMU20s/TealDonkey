import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question( models.Model):
    def __str__(self):
        return self.question_texts
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=1)
    question_texts = models.CharField(max_length=200) #Set max charactor question
    pub_date = models.DateTimeField('date published') #Set published date



class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Make a choose option
    choice_text = models.CharField(max_length=200) # Make choice text
    votes = models.IntegerField(default=0) #Amount of people who chose this vote