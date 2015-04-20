#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Monk-ee (magic.monkee.magic@gmail.com).
#
# Requires: your boto config file (~/.boto) to contain your aws credentials
#
# [Credentials]
# aws_access_key_id = <your access key>
# aws_secret_access_key = <your secret key>

__project__ = 'AWSBillingToDynamoDB'
__author__ = "monkee"
__version__ = "1.0.1"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

"""
core.py - A python script to collect biling reports and transfer them to dynamodb for querying.

Copyright (C) 2015 Lyndon Swan <magic.monkee.magic@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

"""

class AWSBillingTODynamoDB():
    """
    Connects to an S3 Billing Bucket and converts the files to a DynamoDB

    """
    billing_bucket = "cloudtrek-billing"
    dynamodb_table = "billing"


    def __init__(self):
        self.check_bucket_access()
        self.check_dynamodb_tables()

    def check_bucket_access(self):
        pass

    def check_dynamodb_tables(self):
        pass



