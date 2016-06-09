from collections import OrderedDict
import inspect
import itertools
import operator


def _get_defined_methods(cls):
    '''
    Get all the methods that are defined on *that* class, ignoring parents.
    '''
    ret = []
    for name, val in cls.__dict__.items():
        if inspect.isfunction(val):
            lines, lnum = inspect.getsourcelines(val)
            ret.append((name, inspect.getsource(val), lnum))
    ret.sort(key=operator.itemgetter(2))
    return list(map(operator.itemgetter(0, 1), ret))


def flatten(cls):
    methods = OrderedDict()
    for subcls in cls.__mro__[-2::-1]:
        methods.update(_get_defined_methods(subcls))

    body = '\n'.join(methods.values()) or '    pass\n'
    return 'class {}(object):\n{}'.format(cls.__name__, body)
