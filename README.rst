========================================================
``def_main``: a tiny decorator to define main
========================================================

Define a Python main function in one step - no more `__main__`!

For any non-trivial projects, use typer and dtyper instead!

How to install
==================

Use ``pip``:

.. code-block:: bash

    pip install def_main

Usage examples
==================

Without an return code
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import def_main

    @def_main
    def main(*argv):
        print('hello,', *argv)


means precisely the same as:

.. code-block:: python

    def main(*argv):
        print('hello,', *argv)


    if __name__ == '__main__':
        import sys

        main(sys.argv[1:])

With a return code
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python


    import def_main

    @def_main
    def main(*argv):
        print('hello,', *argv)
        return argv


means precisely the same as:

.. code-block:: python

    def main(*argv):
        print('hello,', *argv)
        return argv


    if __name__ == '__main__':
        import sys

        returncode = main(sys.argv[1:])
        sys.exit(returncode)
