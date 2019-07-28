#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='PyClosure',
    version='0.0.1',
    description='A simple to allow to make compiling JavaScript with the Closure compiler easier.',
    long_description=readme,
    author='Stanley Lim',
    author_email='slim679975@gmail.com',
    url='https://github.com/Spiderpig86/PyClosure',
    license=license,
    packages=find_packages(exclude=('tests')),
    python_requires='>=3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools'
    ]
)
