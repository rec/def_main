import def_main


@def_main
def main(message='you!', *rest):
    print('test_main says hello!, to', message, *rest)


@def_main
def error(*argv):
    print('error!')
    return 1


@def_main
def never_reached(*argv):
    print('This is never reached')
    return 0
