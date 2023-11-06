import json

from django.http import HttpResponse
from app.models.authentication import ExpiringTokenAuthentication
from app.models.Players import Players 
from app.serializers.playersSerializer import PlayersSerializer
from rest_framework import authentication, permissions, generics, status


class PlayersView(generics.ListAPIView):
    query_set = Players.objects.all()
    serializer_class = PlayersSerializer
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all players
        """
        response_status = status.HTTP_200_OK
        serializer = PlayersSerializer(self.query_set, many=True)
        if not serializer.data:
            response_status = status.HTTP_404_NOT_FOUND
        response_data = {}
        response_data['status'] = response_status
        response_data['data'] = serializer.data
        
        return HttpResponse(json.dumps(response_data, indent=4), content_type="application/json", status=response_status)