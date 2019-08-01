#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='PyClosure',
    version='0.0.1',
    description='A simple to allow to make compiling JavaScript with the Closure compiler easier.',
    long_description=readme,long_description_content_type='text/markdown',
    author='Stanley Lim',
    author_email='slim679975@gmail.com',
    url='https://github.com/Spiderpig86/PyClosure',
    license='MIT License',
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
            'pyclosure = pyclosure.__main__:main',
        ],
    },
)
