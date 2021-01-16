# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

with open(path.join(here, 'src/QieyunEncoder/version.py'), encoding='utf8') as f:
    exec(f.read())

setup(
    name='qieyun-encoder',
    version=__version__,
    description='Convert a phonological position of the Qieyun phonological system to the three-character phonological encoding and the phonological description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nk2028/qieyun-encoder',
    author='Ngiox Khyen 2028 Project',
    author_email='support@nk2028.shn.hk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Chinese (Traditional)',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='middle-chinese historical-linguistics qieyun',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.5, <4',
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/nk2028/qieyun-encoder/issues',
        'Source': 'https://github.com/nk2028/qieyun-encoder',
    }
)
