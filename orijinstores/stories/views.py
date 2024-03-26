from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Story
from .serializers import StorySerializer

class StoriesApiView(APIView):
    def get(self, request, *args, **kwargs):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    