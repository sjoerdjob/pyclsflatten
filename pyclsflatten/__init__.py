"""
Python class flattener

A tool to get a flattened impression of a class hierarchy.

For example, in the Django framework, `django.views.generic.edit.UpdateView` is
composed of a lot of subclasses through a subclassing hierarchy.

By running it through the `pyclsflatten` tool, you can get an impression of all
the components that make it work in a linear manner.
"""
from collections import OrderedDict
import inspect
import operator


def _get_defined_methods(cls):
    """
    Get all the methods that are defined on *that* class, ignoring parents.
    """
    ret = []
    for name, val in cls.__dict__.items():
        if inspect.isfunction(val):
            lines, lnum = inspect.getsourcelines(val)
            ret.append((name, ''.join(lines), lnum))
    ret.sort(key=operator.itemgetter(2))
    return [(name, source) for name, source, lnum in ret]


def flatten(cls):
    """
    Get a flattened imitation of a class definition.

    The returned definition is not necessarily correct.
    """
    methods = OrderedDict()
    for subcls in cls.__mro__[-2::-1]:
        methods.update(_get_defined_methods(subcls))

    metaclass = type(cls)
    if metaclass is not type:
        base = 'metaclass=' + metaclass.__name__
        flat_mc = flatten(metaclass) + '\n\n'
    else:
        # Oddly enough, `type.__mro__ == (type, object)`. Weird, huh?
        # But yes, we need to deal with that.
        base = 'type' if type in cls.__mro__ else 'object'
        flat_mc = ''

    body = '\n'.join(methods.values()) or '    pass\n'
    return '{flat_mc}class {name}({base}):\n{body}'.format(
        flat_mc=flat_mc,
        base=base,
        name=cls.__name__,
        body=body
    )
