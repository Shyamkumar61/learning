def add(*args):
    value = 0
    for arg in args:
        value += arg
    return value


def mult(*args):
    value = 1
    for arg in args:
        value *= arg
    return value