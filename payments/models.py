# payments/models.py
import uuid
from django.db import models
from django.conf import settings 

class Transaction(models.Model):
    STATUS_CHOICES = [
        ("created","Created"), ("processing","Processing"),
        ("succeeded","Succeeded"), ("failed","Failed"),
        ("refunded","Refunded"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey('jobs.Job', on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    initiator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='initiated_transactions')
    stripe_payment_intent = models.CharField(max_length=200, unique=True, null=True, blank=True)
    stripe_charge_id = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="USD")
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)