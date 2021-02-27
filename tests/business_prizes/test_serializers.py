import pytest
import sys
from business_prizes.api.business import BusinessSerializer
from business_prizes.api.product import ProductSerializer


repr_business_serializer = \
"""
BusinessSerializer():
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=50, style={'base_template': 'textarea.html'})
    description = CharField(style={'base_template': 'textarea.html'})
    email = EmailField(max_length=254)
    address = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
    website = URLField(allow_blank=True, allow_null=True, max_length=200, required=False)
"""

repr_product_serializer = \
"""
ProductSerializer():
    id = IntegerField(label='ID', read_only=True)
    name = CharField(style={'base_template': 'textarea.html'})
    description = CharField(style={'base_template': 'textarea.html'})
    value = CharField(allow_blank=True, allow_null=True, required=False, style={'base_template': 'textarea.html'})
"""


@pytest.mark.parametrize('serializer, repr_string', [
    (BusinessSerializer(), repr_business_serializer),
    (ProductSerializer(), repr_product_serializer),
])
def test_business_serializer1(serializer, repr_string, capsys):
    print(f'\n{repr(serializer)}')
    captured = capsys.readouterr()
    assert captured.out == repr_string
