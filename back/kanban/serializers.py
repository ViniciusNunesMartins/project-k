from rest_framework import serializers
from .models import Dashboard, Board, Card, Comment



class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')