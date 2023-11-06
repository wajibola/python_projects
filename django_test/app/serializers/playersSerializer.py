from rest_framework import serializers

from app.models.Players import Players

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'