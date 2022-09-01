SETUP_DESC = {
    'name': 'def_main',
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ],
    'description': 'A simple definition of main',
    'keywords': ['main function'],
    'license': 'MIT',
    'long_description': open('README.rst').read(),
    'py_modules': ['def_main'],
    'url': 'https://github.com/rec/def_main',
}

if __name__ == '__main__':
    from setuptools import setup
    import def_main

    setup(
        version=def_main.__version__,
        **SETUP_DESC
    )
