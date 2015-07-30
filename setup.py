#!/usr/bin/env python

import os
import sys

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

if sys.argv[-1] == 'publish':
  os.system('python setup.py sdist upload')
  sys.exit()

requires = [
  'requests==2.6.0'
]

setup(
  name='constant-contact-python',
  version='0.0.2',
  description='Api sdk for constantcontact.com',
  author='Jordan Clark',
  author_email='jordan@blitzen.com',
  packages=['constantcontact'],
  install_requires=requires,
  license='MIT',
  zip_safe=False,
  classifiers=(
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  )
)
