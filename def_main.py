from typing import Callable
import sys


def def_main(f: Callable) -> Callable:
    if f.__module__ == '__main__':
        f(*sys.argv[1:])

    return f


sys.modules['def_main'] = def_main
def_main.__version__ = '0.10.0'


@def_main
def main(*argv):
    print('def_main says hello!, to', *argv)
