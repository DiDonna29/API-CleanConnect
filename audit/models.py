# audit/models.py
from django.db import models
from django.conf import settings

class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action_type = models.CharField(max_length=200)
    target_type = models.CharField(max_length=200) 
    target_id = models.CharField(max_length=200, blank=True, null=True) 
    detail = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)