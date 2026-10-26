from django.db import models
# Create your models here.

"""
Schema Name: QuestionsDb
fields:title,language,difficulty_level,topic,score
"""

class QuestionsDb(models.Model):
    title=models.CharField(max_length=200)
    LANGUAGE_CHOICES=(
        ('python','Python'),
        ('java','Java'),
        ('c++','C++'),
    )
    language=models.CharField(max_length=200,choices=LANGUAGE_CHOICES)
    DIFFICULTY_CHOICES=(
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard')
    )
    difficulty_level=models.CharField(max_length=200,choices=DIFFICULTY_CHOICES)
    score=models.IntegerField()
    topic=models.CharField(max_length=100)
    note=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    sample_input=models.TextField()
    sample_output=models.TextField()
    is_active=models.BooleanField(default=True)

class SubmissionDb(models.Model):
    answer=models.TextField()
    question_id=models.IntegerField()
    owner=models.CharField(max_length=200)
    points=models.PositiveIntegerField(null=True)
    submission_date=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(null=True)    