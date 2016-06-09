import inspect


def flatten(cls):
    body = ''.join(inspect.getsourcelines(cls)[0][1:])
    return 'class {}(object):\n{}'.format(cls.__name__, body)
