import inspect


def flatten(cls):
    return inspect.getsource(cls)
