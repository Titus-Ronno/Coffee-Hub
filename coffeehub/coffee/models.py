from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price= models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

class Card(models.Model):
    image = models.CharField(max_length=2083)
    title = models.CharField(max_length=100)
    text = models.TextField()

class Reply(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.image.name

class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    details = models.TextField()

    def __str__(self):
        return f"Training Session for {self.user.username} on {self.date}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
