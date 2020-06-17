from rest_framework import serializers
from business_prizes.models import Business, Product

__all__ = ['BusinessSerializer', 'ProductSerializer']


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'description', 'email', 'address', 'website')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'value')
