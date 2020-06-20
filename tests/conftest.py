import pytest


@pytest.fixture
def businesses_data():
    return [
        {
            'name': 'Turkish Shop',
            'description': 'Sells stuffs.',
            'email': 'turkish-email@alpha.com',
            'address': 'Ataturk 13',
            'website': 'turkish-website.com'
        },
        {
            'name': 'Greek Shop',
            'description': 'Grosery store.',
            'email': 'greek-email@alpha.com',
            'address': 'Seferi 2',
            'website': 'greek-website.com'
        }
    ]

@pytest.fixture
def products_data():
    return [
        {
            'name': 'Mango Juice',
            'description': 'Delicious sugar-free 1 litre mango juice.',
        },
        {
            'name': 'Rosemary plant',
            'description': 'A fresh Rosemary plant.',
        },
        {
            'name': 'Feta cheese',
            'description': 'One kilo of feta cheese.',
        },
        {
            'name': 'Tavli boardgame',
            'description': 'A portable backgammon board game.',
        }
    ]


@pytest.fixture
def code_generator(db):
    from lottery.db_access.models import Participation
    from lottery.utils import CodeGenerator
    def _code_generator(code_length, nb_codes):
        return CodeGenerator.from_lottery_db(code_length, nb_codes, Participation, update=True)
    return _code_generator


@pytest.fixture
def competition_maker(code_generator):
    from lottery.db_access.models import Competition, ParticipationsTable
    def _competition_maker(name, begin, end, code_length, nb_codes):
        c = Competition(name=name, begin_date=begin, end_date=end, is_running=True)
        c.save()
        ParticipationsTable.objects.new_random(c, code_generator(code_length, nb_codes))
        return c
    return _competition_maker


@pytest.fixture
def test_competition(competition_maker):
    import datetime
    def _test_competition(name, duration, code_length, nb_codes):
        now = datetime.date.today()
        delta = datetime.timedelta(days=duration)
        return competition_maker(name, now, now + delta, code_length, nb_codes)
    return _test_competition


# Test clients

@pytest.fixture
def clients(client, business_client, admin_client):
    return {
        'anonymous': client,
        'business': business_client,
        'admin': admin_client
    }

@pytest.fixture
def business_client(client, django_user_model):
    username = "greek_business"
    password = "strong_password"
    django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    return client
