""" pycinga a python module to access icinga via rest api """

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
 long_description = f.read()

setup(
name='pycinga',
version='0.0',
description='module to access icinga via rest api',
long_description=long_description,
url='https://github.com/hpfmn/pyuci',
author='Johannes "hpfmn" Wegener',
author_email='mail@johanneswegener.de',
classifiers=[
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Programming Language :: Python :: 3.4'
],
keywords='icinga',
packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
install_requires=['requests', 'json']
)
