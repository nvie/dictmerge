"""
Merge dicts without mutating them.
"""
from setuptools import setup

setup(
    name='dictmerge',
    version='0.1.2',
    url='https://github.com/nvie/dictmerge',
    license='BSD',
    author='Vincent Driessen',
    author_email='me@nvie.com',
    description='Merge dicts without mutating them.',
    long_description=__doc__,
    py_modules=['dictmerge'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
