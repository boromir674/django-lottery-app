from django.test import TestCase

import pytest

from django.urls import reverse
from django.contrib.auth.models import AnonymousUser

from lottery.views.winner import CodeChecker


####### DATA
@pytest.fixture()
def user():
    return AnonymousUser()

@pytest.fixture()
def setup_response():
    return {
        'get': {
            'code': 200,
            'content': lambda x: x == ''
        },
        'post': {
            'code': 200,
            'content': lambda x: x == ''
        }
    }

##### FACTORIES
@pytest.fixture
def request_factory(rf):
    method = {'get': rf.get,
              'post': rf.post}
    def _request_factory(**kwargs):
        request = method[kwargs['method']](reverse('lottery_index'), **kwargs.get('data', {}))
        request.user = kwargs['user']
        request.follow = True
        return request
    return _request_factory

##### TESTS
@pytest.mark.parametrize(
    'method', [
        'get',
        'post',
    ]
)
def test_responses(method, request_factory, user, setup_response): # user, expected_code, expected_content, request_factory, users):
    request = request_factory(user=user, method=method)
    response = CodeChecker.as_view()(request)
    assert setup_response[method]['code'] == response.status_code
    assert b'DD Lottery App' in response.content
    # assert setup_response[method]['content'](response.content)
