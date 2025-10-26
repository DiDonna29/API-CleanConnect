# reviews/admin.py
from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('job', 'author', 'target', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('author__email', 'target__email', 'comment')