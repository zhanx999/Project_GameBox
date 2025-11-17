from rest_framework import serializers
from .models import Game, Screenshot, Comment

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['id', 'image', 'game']

class GameSerializer(serializers.ModelSerializer):
    screenshots = ScreenshotSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'image', 'description', 'release_date', 'genre',
            'developer', 'publisher', 'platform', 'edition', 'os_req', 'cpu_req',
            'ram_req', 'gpu_req', 'disk_req', 'slug', 'video_url', 'screenshots'
        ]

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    game = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'game', 'author', 'content', 'created_at']
