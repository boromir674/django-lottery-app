from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from business_prizes.models import Business, Product


# Serialization
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'value')


# API
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer  # s(partial=True)

    _locked = False

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, flag):
        self._locked = flag

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ('list', 'retrieve'):
            return [IsAuthenticatedOrReadOnly, IsAdmin]
        if self._locked:  # if competition has started, then business should not be able to modify their data (I guess)
            return [IsAdminUser]
        return [IsAuthenticated, IsAdmin]
    #
    # def list(self, request):
    #     pass
    #
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass

    def get_queryset(self):
        if get_user_model.is_staff:  # can access the admin site
            return Product.objects.all()
        business = Business.objects.get(user=self.request.user)
        return Product.objects.get(business=business)
