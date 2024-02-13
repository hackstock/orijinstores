from django.contrib import admin

from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at"]
    list_filter = ["created_at", "price"]
    search_fields = ["title", "description"]

admin.site.register(Story, StoryAdmin)
