import attr
import random
import string


@attr.s
class StringCreator:
    character_set = attr.ib(init=True)
    string_length = attr.ib(init=True, default=8)

    def build(self):
        """Call this method to get a string of random letters, digits and symbols."""
        return self.digits_and_symbols(length=self.string_length)

    def digits_and_symbols(self, length=10):
        return ''.join(random.choice(self.character_set) for i in range(length))

    @classmethod
    def from_django_settings(cls, string_length):
        from django.conf import settings
        return StringCreator(settings.PASSWORD_CHARACTERS, string_length)

    @classmethod
    def default_character_set(cls, string_length=6):
        return StringCreator(string.ascii_lowercase + string.ascii_uppercase + '!"#$%&()*+,-./:;<=>?@[]^_|~', string_length)


class CodeCreator:
    def __init__(self, builder, **kwargs):
        self.builder = builder
    # codes = attr.ib(init=True, default=set, converter=set)

    _instance = None
    def __new__(cls, *args, **kwargs):
        """Possible optional keys: 'codes' and 'init'"""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.codes = set()
        codes = kwargs.get('codes', [])
        if codes:
            if kwargs.get('init', False):
                cls._instance.codes = codes
            else:
                cls._instance.codes.update(codes)
        return cls._instance

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

    @classmethod
    def from_django_settings(cls, code_length, **kwargs):
        """
        :param int code_length:
        :param kwargs: action1: if 'codes' and 'init'=True, sets seen_codes=kwargs['codes']; action2: if 'codes', updates seen_codes.add(kwargs['codes'])
        :return:
        """
        return CodeCreator(StringCreator.from_django_settings(code_length), **kwargs)

    @classmethod
    def from_lottery_db(cls, code_length, participation_model, **kwargs):
        """Initializes the singleton CodeCreator instance with the codes from the current db state and returns the object\n
        :param kwargs: action1: if 'init'=False, then updates the potentially existant codes with the ones from the db. If 'init'=True or not in kwargs then sets the codes witht the ones from the db
        """
        return cls.from_django_settings(code_length,
                                        codes=[p.code for p in participation_model.objects.all()],
                                        init=kwargs.get('init', True))


@attr.s
class CodeGenerator:
    builder = attr.ib(init=True)
    _nb_codes = attr.ib(init=True)

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def seen_codes(self):
        return self.builder.codes

    @seen_codes.setter
    def seen_codes(self, codes):
        """Indicate codes that should be skipped if they happen to be generated"""
        self.builder.codes = set(codes)

    @property
    def code_length(self):
        """Return the number of characters the random codes will contain."""
        return self.builder.builder.string_length

    @code_length.setter
    def code_length(self, code_length):
        """Set the number of characters the random codes will contain"""
        self.builder.builder.string_length = code_length

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
    def from_django_settings(cls, code_length, nb_codes, **kwargs):
        """
        :param int code_length:
        :param int nb_codes:
        :param kwargs: action1: if 'codes' and 'init'=True, sets seen_codes=kwargs['codes']; action2: if 'codes', updates seen_codes.add(kwargs['codes'])
        :return:
        """
        return CodeGenerator(CodeCreator.from_django_settings(code_length, **kwargs), nb_codes)

    @classmethod
    def from_lottery_db(cls, code_length, nb_codes, participation_model, **kwargs):
        """Returns the singleton object by initializing the 'seen' codes with the ones in the db. Pass 'update'=True to update the 'seen' codes instead of overwrite."""
        return CodeGenerator(CodeCreator.from_lottery_db(code_length, participation_model, init=not kwargs.get('update', False)), nb_codes)


if __name__ == '__main__':

    cg = CodeGenerator(CodeCreator(StringCreator.default_character_set(string_length=4)), 7)
    codes = [c for c in cg]

    assert len(codes) == 7
    assert all(len(c) == 4 for c in codes)

    print('\n'.join(codes))
