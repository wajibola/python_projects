from rest_framework import serializers

from app.models.Positions import Positions

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'