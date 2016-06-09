from unittest import TestCase

from pyclsflatten import flatten


class SimpleBase(object):
    pass


class SimpleExtension(SimpleBase):
    pass


class LinearExampleTests(TestCase):
    def test_simple(self):
        output = flatten(SimpleExtension)
        self.assertEqual(output, """\
class SimpleExtension(object):
    pass
""")
