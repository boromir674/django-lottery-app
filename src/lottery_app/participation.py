import attr

import random


@attr.s
class StringCreator:
    character_set = attr.ib(init=True)
    string_length = attr.ib(init=True, default=8)

    def build(self):
        """Call this method to get a string of random letters, digits and symbols."""
        return self.digits_and_symbols(length=self.string_length)

    def digits_and_symbols(self, length=10):
        return ''.join(random.choice(Str.character_set) for i in range(length))


@attr.s
class CodeCreator:
    builder = attr.ib(init=True)
    codes = attr.ib(init=True, default=set, converter=set)

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
    builder = attr.ib(init=True)
    _nb_codes = attr.ib(init=True)

    @property
    def seen_codes(self):
        return self.builder.codes

    @seen_codes.setter
    def seen_codes(self, codes):
        """Indicate codes that should be skipped if they happen to be generated"""
        self.builder.codes = set(codes)

    @property
    def nb_codes(self):
        """Number of codes the generator will emmit"""
        return self._nb_codes

    @nb_codes.setter
    def nb_codes(self, nb_codes):
        """Set the number of codes the generator will emmit"""
        self._nb_codes = nb_codes

    def __iter__(self):
        return iter(self.builder.get_code() for _ in range(self._nb_codes))

    @classmethod
    def from_django_settings(cls, code_length, nb_codes, seen_codes=None):
        from django.conf import settings
        if seen_codes is None:
            seen_codes = set()
        return CodeGenerator(CodeCreator(StringCreator(settings.PASSWORD_CHARACTERS, code_length), seen_codes), nb_codes)
