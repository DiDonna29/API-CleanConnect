# media/models.py
import uuid
from django.db import models
from django.conf import settings

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='media')
    url = models.URLField()
    type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)