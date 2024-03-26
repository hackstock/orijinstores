from rest_framework import serializers
from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            "title",
            "description",
      
            "artwork",
            "audio_file",
            "author",
        ]