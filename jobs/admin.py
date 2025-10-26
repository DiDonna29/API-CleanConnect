# jobs/admin.py
from django.contrib import admin
from .models import Job, Application

# Personalización del listado de Jobs
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'status', 'assigned_to', 'scheduled_at', 'budget')
    list_filter = ('status', 'scheduled_at', 'location')
    search_fields = ('title', 'description')
    date_hierarchy = 'scheduled_at'

# Personalización del listado de Applications
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'cleaner', 'status', 'bid_amount', 'created_at')
    list_filter = ('status',)
    search_fields = ('job__title', 'cleaner__email')
    # constraint único (job, cleaner) está implícito en el modelo