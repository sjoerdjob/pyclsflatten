from unittest import TestCase

from pyclsflatten import flatten


class SimpleBase(object):
    pass


class SimpleExtension(SimpleBase):
    pass


class ComplexBase(object):
    def methodA(self):
        pass


class ComplexExtension(ComplexBase):
    def methodB(self):
        pass


class LinearExampleTests(TestCase):
    def test_simple(self):
        output = flatten(SimpleExtension)
        self.assertEqual(output, """\
class SimpleExtension(object):
    pass
""")

    def test_complex(self):
        output = flatten(ComplexExtension)
        self.assertEqual(output, """\
class ComplexExtension(object):
    def methodA(self):
        pass

    def methodB(self):
        pass
""")
