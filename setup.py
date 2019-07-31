#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE.txt', 'r', encoding='utf-8') as f:
    license = f.read()

setup(
    name='PyClosure',
    version='0.0.1',
    description='A simple to allow to make compiling JavaScript with the Closure compiler easier.',
    long_description=readme,long_description_content_type='text/x-rst',
    author='Stanley Lim',
    author_email='slim679975@gmail.com',
    url='https://github.com/Spiderpig86/PyClosure',
    license=license,
    packages=find_packages(exclude=('tests')),
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools'
    ],
    entry_points={
        'console_scripts': [
            'pyclosure = __main__:main',
        ],
    },
)
