import pytest

@pytest.fixture
def bussiness_users(django_user_model, businesses_data):
    return [django_user_model.objects.create_user(username=d['name'].lower(), password='strong_password') for d in businesses_data]

@pytest.fixture
def businesses(db, businesses_data, bussiness_users):
    from business_prizes.models import Business, Receit
    receit = Receit.objects.create(width=3)
    receit.save()
    _ = []
    for business_dict, user in zip(businesses_data, bussiness_users):
        _.append(Business.objects.create(**dict({'user': user, 'receit': receit}, **business_dict)))
        _[-1].save()
    return _


@pytest.fixture
def products(db, businesses, products_data):
    from business_prizes.models import Product
    _ = []
    businesses_data_structure = [x for pair in zip(businesses, businesses) for x in pair]
    for product_dict, business in zip(products_data, businesses_data_structure):
        _.append(Product.objects.create(**dict({'business': business}, **product_dict)))
        _[-1].save()
    return _

# @pytest.mark.skip
@pytest.mark.parametrize('name, duration, code_length, nb_codes', [
    ('testauto-competition', 1, 3, 10)
])
def test_endpoints(name, duration, code_length, nb_codes, businesses, products, test_competition):
    competition = test_competition(name, duration, code_length, nb_codes)
