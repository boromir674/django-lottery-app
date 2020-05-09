import attr

import random
import string


@attr.s
class StringCreator:
    string_length = attr.ib(init=True, default=8)

    def build(self):
        return self.digits_and_symbols(length=self.string_length)

    def digits_and_symbols(self, length=10):
        """Call this method to get a string of random letters, digits and symbols."""
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(length))


@attr.s
class CodeCreator:
    length = attr.ib(init=True, converter=int)

    codes = attr.ib(init=True, default=set, converter=set)
    builder = attr.ib(init=False, default=attr.Factory(lambda self: StringCreator(self.length), takes_self=True))

    def get_code(self):
        code = self._build_code()
        while not code:  # account for the impossible; duplicate code!
            code = self._build_code()
        return code

    def _build_code(self):
        _ = self.builder.build()
        if _ not in self.codes:
            self.codes.add(_)
            return _
        return None  # return None to indicate failure in case our builder happens to build a code already seen


@attr.s
class CodeGenerator:
    length = attr.ib(init=True)
    _nb_codes = attr.ib(init=True)
    _seen_codes = attr.ib(init=True, default=set, converter=set)

    builder = attr.ib(init=True, default=attr.Factory(lambda self: CodeCreator(self.length, self._seen_codes), takes_self=True))
    _gen = attr.ib(init=False, default=None)
    # _gen = attr.ib(init=False, default=attr.Factory(lambda self: iter(self.builder.get_code() for _ in range(self.length)), takes_self=True))

    @property
    def seen_codes(self):
        return self.builder.codes

    @property
    def nb_codes(self):
        """Number of codes the generator will emmit"""
        return self._nb_codes

    @nb_codes.setter
    def nb_codes(self, nb_codes):
        """Set the number of codes the generator will emmit"""
        self._nb_codes = nb_codes

    def __iter__(self):
        self._gen = iter(self.builder.get_code() for _ in range(self._nb_codes))

    @classmethod
    def create(cls, code_legth, nb_codes, seen_codes=None):
        if seen_codes is None:
            seen_codes = []
        return CodeGenerator(code_legth, nb_codes, CodeCreator(code))

