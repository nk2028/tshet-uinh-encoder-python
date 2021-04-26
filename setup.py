# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

setup(
    name='qieyun-encoder',
    version='0.4.0',
    description='A Python library for the operating the basic structure of the Qieyun phonological system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nk2028/qieyun-encoder-python',
    author='The nk2028 Project',
    author_email='support@nk2028.shn.hk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Chinese (Traditional)',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='middle-chinese historical-linguistics qieyun',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6, <4',
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/nk2028/qieyun-encoder-python/issues',
        'Source': 'https://github.com/nk2028/qieyun-encoder-python',
    }
)
