from django.contrib.auth import get_user_model
from rest_framework import viewsets


class BaseModelViewSet(viewsets.ModelViewSet):
    """Abstraction to automate permission definition."""
    def get_permissions(self):
        """Instantiates and returns the list of permissions that this view requires."""
        return [permission() for permission in self._get_permissions()]

    def _get_permissions(self):
        """This method must return an iterable with permission types (see rest_framework.permissions)."""
        raise NotImplementedError
