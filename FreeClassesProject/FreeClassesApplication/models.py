from django.db import models

# Create your models here.
class ClassData(models.Model):
    instname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)
    venue = models.CharField(max_length=100)

class FeedbackData(models.Model):
    instname = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField()
    feedback = models.TextField(max_length=10000)

class MessageData(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    message = models.TextField(max_length=10000)


class DocumentData(models.Model):
    subject = models.CharField(max_length=100)
    files  = models.FileField(upload_to='files')


    def __str__(self):
        return self.subject