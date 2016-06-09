from unittest import TestCase

from pyclsflatten import flatten


class Simple(object):
    pass


class SomethingWithDefinitions(object):
    def get_name(self):
        return 'foo'


class FlatExampleTests(TestCase):
    def test_simple(self):
        output = flatten(Simple)
        self.assertEqual(output, """\
class Simple(object):
    pass
""")

    def test_something_with_definitions(self):
        output = flatten(SomethingWithDefinitions)
        self.assertEqual(output, """\
class SomethingWithDefinitions(object):
    def get_name(self):
        return 'foo'
""")
