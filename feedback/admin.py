# Register your models here.
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'message')
    search_fields = ('user__username', 'message')
# Register your models here.
