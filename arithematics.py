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


def div(*args):
    value = 0
    if len(args) >= 2:
        for arg in range(0, len(args) - 1):
            value = args[arg]/args[arg + 1]
    return value


def sum(*args):
    value = 0
    for arg in range(0, len(args) - 1):
        value -= args[arg]
    return value