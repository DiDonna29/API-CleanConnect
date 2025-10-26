# jobs/models.py
import uuid
from django.db import models
from django.conf import settings 

class Job(models.Model):
    STATUS_CHOICES = [
        ("draft","Draft"),
        ("open","Open"),
        ("assigned","Assigned"),
        ("in_progress","In Progress"),
        ("completed","Completed"),
        ("cancelled","Cancelled"),
        ("paid","Paid"),
        ("disputed","Disputed"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_jobs')
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    required_services = models.JSONField(default=list, blank=True)
    preferred_cleaner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='preferred_jobs')
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft", db_index=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assignments')
    scheduled_at = models.DateTimeField(null=True, blank=True)
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Application(models.Model):
    STATUS_CHOICES = [
        ("pending","Pending"),
        ("accepted","Accepted"),
        ("rejected","Rejected"),
        ("withdrawn","Withdrawn"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    cleaner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    message = models.TextField(blank=True)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('job', 'cleaner')