#!/usr/bin/env python

import os
from setuptools import setup, find_packages

setup(name='unbabel_subword_nmt',
      version='0.2.0',
      description='Subword through Byte Pair Encoding',
      author='Unbabel',
      author_email='support@unbabel.com',
      packages=find_packages(),
      install_requires=[],
      url='https://github.com/Unbabel/subword-nmt',
      classifiers=['Intended Audience :: Unbabel',
                   'Programming Language :: Python '],
      license='BSD 3-clause',
      include_package_data=True)
