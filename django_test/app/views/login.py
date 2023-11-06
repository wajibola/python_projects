import json
from django.contrib.auth import authenticate
from django.http import HttpResponse

from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from datetime import timedelta

from project import settings

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data,
                                                     context = {'request': request})
            if login_serializer.is_valid():
                user = login_serializer.validated_data['user']
                
                token, created = Token.objects.get_or_create(user=user)
                print(f"Created: {created}")
                
                return HttpResponse(json.dumps({'token': token.key, 
                                                'expiration_date': token.created + timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)},
                                                indent=4, default=str), 
                                    content_type="application/json", 
                                    status=status.HTTP_200_OK)
            
            return HttpResponse(json.dumps({'detail': 'Invalid Credentials'}, indent=4), 
                                    content_type="application/json", 
                                    status=status.HTTP_400_BAD_REQUEST)
        
        return HttpResponse(json.dumps({'detail': 'Invalid Credentials'}, indent=4), 
                            content_type="application/json", 
                            status=status.HTTP_400_BAD_REQUEST)