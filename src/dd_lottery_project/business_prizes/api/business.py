from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import views
from business_prizes.models import Business

from .base_model_view_set import BaseModelViewSet

import logging

logger = logging.getLogger(__name__)


# Serialization
class BusinessSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Business
        fields = ('id', 'name', 'description', 'email', 'address', 'website')
        read_only_fields = ('id',)


# class BusinessApiViewSet(views.APIView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = BusinessSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessViewset(BaseModelViewSet):
    serializer_class = BusinessSerializer
    search_fields = ('name', 'email', 'address', 'website')
    queryset = Business.objects.all()

    def _get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [AllowAny]
        if self.action in ('update', 'partial_update', 'create'):
            return [IsAuthenticated, IsAdminUser]
        return [IsAdminUser]  # if self.action == 'destroy'

    def list(self, request, *args, **kwargs):
        businesses = Business.objects.all()
        bus_serializer = BusinessSerializer(businesses, many=True)
        return Response(bus_serializer.data)

    def create(self, request, *args, **kwargs):
        business = None
        try:
            business = Business.objects.get(user.request.user)
        except Business.exception.NotFoundError as e:
            logger.info(f"Did not find an existing Business registered for user {request.user.username}")
        if business is None:
            try:
                business = Business(user=request.user, name=request.data['name'], description=request.data['description'], email=request.data['email'],
                                address=request.data['address'], website=request.data['website'])
                business.save()
            except Exception as e:
                logger.error(e)
                return Response(data={'event': {
                    'type': 'error',
                }}, status=400)
            return Response(data={'event': {
                'type': 'creation',
                'id': business.pk,
            }}, status=201)
        return Response(data={'event': {
                'type': 'none',
            }}, status=403)  # "the server understood the request, but is refusing to authorize it: https://en.wikipedia.org/wiki/HTTP_403


if __name__ == '__main__':
    serializer = BusinessSerializer()
    print(repr(serializer))