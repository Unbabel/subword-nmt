#!/usr/bin/env python

import os
import setuptools

setuptools.setup(
    name='unbabel-subword-nmt',
    version='0.1dev',
    description='Subword through Byte Pair Encoding',
    long_description=open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'README.md')).read(),
    license='BSD 3-clause',
    url='https://github.com/Unbabel/subword-nmt'
)