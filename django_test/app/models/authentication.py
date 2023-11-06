import os
import binascii

from django.db import models
from django.utils import timezone

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

from datetime import timedelta

from project import settings

def token_is_expired(token):
    return timezone.now() > token.created + timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)

""" class ExpiringToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    expiration_date = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.key:
            print("generating token")
            self.key = self.generate_token()

        self.expiration_date = timezone.now() + timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)
        return super(ExpiringToken, self).save(*args, **kwargs)

    def generate_token(self) -> str:
        return binascii.hexlify(os.urandom(25)).decode()

    def __str__(self):
        return self.key """
    
# DEFAULT_AUTHENTICATION_CLASSES
class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key = key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid Token")
        
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User is not active")

        is_expired = token_is_expired(token)
        if is_expired:
            token.delete()
            print(f'Token: {token}')
            raise exceptions.AuthenticationFailed("The Token is expired.")
        
        return (token.user, token)