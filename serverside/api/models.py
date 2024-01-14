from djongo import models
from rest_framework import serializers



# Create your models here.
class Subject(models.Model):
    
    name = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=250)
    quizList = models.JSONField(default=list, blank=True, null=True)
    
    class Meta:
            db_table = 'subject_names'

class Quiz(models.Model):
    question = models.CharField(max_length=250)
    options = models.JSONField(default=list, blank=True, null=True)
    quizId = models.CharField(max_length=150)
    correctOption = models.IntegerField()
    imageUrl = models.CharField(max_length=150,null=True)
    
    class Meta:
            db_table = 'quizzes'
    
class QuizNew(models.Model):
    question = models.CharField(max_length=250)
    options = models.JSONField(default=list, blank=True, null=True)
    quizId = models.CharField(max_length=150)
    correctOption = models.IntegerField()
    subject = models.CharField(default='Public Administration' ,max_length=100)
    imageUrl = models.CharField(max_length=150,null=True)
    
    class Meta:
            pass
            
class Result(models.Model):
    
    quizName = models.CharField(max_length=100)
    userId = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    score = models.IntegerField()
    correctAnswers = models.IntegerField()
    totalQuestions = models.IntegerField()
    time = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'user_results'

class AppUser(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    dateOfBirth = models.CharField(max_length=20)
    userId = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'app_users'
    