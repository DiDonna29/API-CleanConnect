# audit/admin.py
from django.contrib import admin
from .models import AuditLog
@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('actor', 'action_type', 'target_type', 'target_id', 'created_at')
    list_filter = ('action_type', 'target_type')
    search_fields = ('actor__email', 'target_id', 'detail')
    readonly_fields = ('actor', 'action_type', 'target_type', 'target_id', 'detail', 'created_at')