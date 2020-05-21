
from lottery.utils import CodeGenerator

import pytest

@pytest.fixture()
def code_generator():
    return CodeGenerator.from_django_settings(4, 10, seen=[], init=True)


def test_code_generator(code_generator):
    codes = [c for c in code_generator]

    assert all(len(c) == 4 for c in codes)
    code_set = set(codes)
    assert len(code_set) == len(codes) == 10