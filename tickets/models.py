from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone=models.CharField(max_length=14,unique=True)

class RoadIssue(models.Model):

    ISSUE_TYPES = (
        ('pothole', 'Pothole'),
        ('drainage', 'Drainage Issue'),
        ('streetlight', 'Street Light Not Working'),
        ('garbage', 'Garbage Dump'),
        ('road_damage', 'Road Damage'),
    )

    STATUS_CHOICES = (
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)

    location = models.CharField(max_length=255)  # simple version
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    image = models.ImageField(upload_to="issues/", null=True, blank=True)

    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reported_issues")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    issue = models.ForeignKey(RoadIssue, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reaction(models.Model):
    issue = models.ForeignKey(RoadIssue, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['issue', 'user']