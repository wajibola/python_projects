import json

from django.http import HttpResponse
from app.models.Positions import Positions
from app.serializers.positionsSerializer import PositionsSerializer
from rest_framework import authentication, permissions, generics, status

class PositionsView(generics.ListAPIView):
    query_set = Positions.objects.all()
    serializer_class = PositionsSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all positions
        """
        response_status = status.HTTP_200_OK
        serializer = PositionsSerializer(self.query_set, many=True)
        if not serializer.data:
            response_status = status.HTTP_404_NOT_FOUND
        response_data = {}
        response_data['status'] = response_status
        response_data['data'] = serializer.data
        
        return HttpResponse(json.dumps(response_data, indent=4), content_type="application/json", status=response_status)
