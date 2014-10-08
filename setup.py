"""
Merge dicts without mutating them.
"""
from setuptools import setup

setup(
    name='dictmerge',
    version='0.1.1',
    url='https://github.com/nvie/dictmerge',
    author='Vincent Driessen',
    author_email='me@nvie.com',
    description='Merge dicts without mutating them.',
    long_description=__doc__,
    py_modules=['dictmerge'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
