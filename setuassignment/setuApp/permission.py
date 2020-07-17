from django.conf import settings

from rest_framework.permissions import BasePermission

class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests

        api_key_secret = request.META.get('HTTP_X_API_KEY')
        print("API KEY")
        print(api_key_secret)
        return api_key_secret == settings.API_KEY_SECRET