from unittest import TestCase

from pyclsflatten import flatten


class Simple(object):
    pass


class SomethingWithOneDefinition(object):
    def get_name(self):
        return 'foo'


class SomethingWithTwoDefinitions(object):
    def get_name(self):
        return 'foo'

    def get_second(self):
        return 'bar'


class FlatExampleTests(TestCase):
    def test_simple(self):
        output = flatten(Simple)
        self.assertEqual(output, """\
class Simple(object):
    pass
""")

    def test_something_with_one_definition(self):
        output = flatten(SomethingWithOneDefinition)
        self.assertEqual(output, """\
class SomethingWithOneDefinition(object):
    def get_name(self):
        return 'foo'
""")

    def test_something_with_two_definitions(self):
        output = flatten(SomethingWithTwoDefinitions)
        self.assertEqual(output, """\
class SomethingWithTwoDefinitions(object):
    def get_name(self):
        return 'foo'

    def get_second(self):
        return 'bar'
""")
