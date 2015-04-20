#!/usr/bin/env python
__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '1.0.1'
setup(
    name='AWSBilllingToDynamoDB',
    version=version,
    description='Python script for converting S3billing reports to DynamoDB',
    url='https://github.io/monk-ee/AWSBillingToDynamoDB',
    download_url=('https://github.io/monk-ee/'
                  'AWSBillingToDynamoDB/archive/%s.tar.gz' % version),
    author='monk-ee',
    author_email='magic.monkee.magic@gmail.com',
    keywords=['aws', 'dynamodb'],
    license='GNU 2.0',
    packages=['AWSBillingToDynamoDB'],
    install_requires = [ 'requests' ],
    test_suite='tests.all_tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GPL v2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ]
)
