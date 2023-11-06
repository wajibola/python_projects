import json

from django.http import HttpResponse
from app.models.authentication import ExpiringTokenAuthentication
from app.models.Teams import Teams
from app.serializers.teamsSerializer import TeamsSerializer
from rest_framework import permissions, generics, status

class TeamsView(generics.ListAPIView):
    query_set = Teams.objects.all()
    serializer_class = TeamsSerializer
    
    authentication_classes = [ExpiringTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all teams
        """
        response_status = status.HTTP_200_OK
        serializer = TeamsSerializer(self.query_set, many=True)
        if not serializer.data:
            response_status = status.HTTP_404_NOT_FOUND
        response_data = {}
        response_data['status'] = response_status
        response_data['data'] = serializer.data
        
        return HttpResponse(json.dumps(response_data, indent=4), content_type="application/json", status=response_status)
    