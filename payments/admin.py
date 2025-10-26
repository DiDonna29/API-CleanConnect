# payments/admin.py
from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'initiator', 'amount', 'status', 'stripe_payment_intent', 'created_at')
    list_filter = ('status', 'currency')
    search_fields = ('stripe_payment_intent', 'job__title', 'initiator__email')
    # Campos de solo lectura (importante para evitar modificar transacciones Stripe)
    readonly_fields = ('stripe_payment_intent', 'stripe_charge_id', 'created_at', 'updated_at')