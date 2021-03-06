"""
    scratchdir
    ~~~~~~~~~~

    Context manager used to maintain your temporary directories/files.

    :copyright: (c) 2017 Andrew Hawker.
    :license: Apache 2.0, see LICENSE for more details.
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_long_description():
    with open('README.rst') as f:
        return f.read()


setup(
    name='scratchdir',
    version='0.0.3',
    author='Andrew Hawker',
    author_email='andrew.r.hawker@gmail.com',
    url='https://github.com/ahawker/scratchdir',
    license='Apache 2.0',
    description='Context manager used to maintain your temporary directories/files.',
    long_description=get_long_description(),
    py_modules=['scratchdir'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    )
)
