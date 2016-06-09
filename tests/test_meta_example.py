from unittest import TestCase

from pyclsflatten import flatten


# Copy-pasted from `six`.
def _with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})


class SimpleMeta(type):
    pass


class Simple(_with_metaclass(SimpleMeta)):
    pass


class MetaExampleTests(TestCase):
    def test_simple_metaclass_definition(self):
        output = flatten(Simple)
        self.assertEqual(output, """\
class SimpleMeta(type):
    pass


class Simple(metaclass=SimpleMeta):
    pass
""")
