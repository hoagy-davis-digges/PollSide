from django.db import models
from datetime import datetime

class Pollster(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    base_url = models.URLField()
    poll_home = models.CharField(max_length=255, null=True)
    poll_regex = models.CharField(max_length=255)
    pdf_regex = models.CharField(max_length=255)

class Poll(models.Model):
    def __str__(self):
        return self.heading
    heading = models.CharField(max_length=255)
    url = models.URLField()
    pollster = models.ForeignKey('Pollster')
    date = models.DateField(default=datetime.now())

class Question(models.Model):
    text = models.TextField()
    poll = models.ForeignKey('Poll')

class Subquestion(models.Model):
    text = models.TextField()
    question = models.ForeignKey('Question')

class Category(models.Model):
    name = models.CharField(max_length=255)
    question = models.ForeignKey('Question', null=True)
    subquestion = models.ForeignKey('Subquestion', null=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category')

class Answer(models.Model):
    text = models.TextField()

class Result(models.Model):
    number = models.IntegerField(null=True)
    percentage = models.IntegerField()
    group = models.ForeignKey('Group')
    answer = models.ForeignKey('Answer')


