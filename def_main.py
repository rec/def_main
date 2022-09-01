from typing import Callable
import sys


def def_main(f: Callable) -> Callable:
    if f.__module__ == '__main__':
        sys.exit(f(*sys.argv[1:]))

    return f


sys.modules['def_main'] = def_main
def_main.__version__ = '0.9.1'


@def_main
def main(*argv):
    print('def_main says hello!, to', *argv)
    return not argv
