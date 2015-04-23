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

import os, logging, sys, yaml
import boto.dynamodb

class AWSBillingTODynamoDB():
    """
    Connects to an S3 Billing Bucket and converts the files to a DynamoDB

    """
    config = ""
    conn = ""


    def __init__(self):
        self.connect()
        self.load_configuration()
        self.check_bucket_access()
        self.check_dynamodb_tables()

    def check_bucket_access(self):
        pass

    def connect(self):
        self.conn = boto.dynamodb.connect_to_region(self.config['general']['region'])

    def check_dynamodb_tables(self):
        try:
            self.conn.get_table(self.config['billing']['dbtables'])
        except Exception as e:
            #we want this error is table is not setup
            if e['error_code'] == 'ResourceNotFoundException':
                self.create_dynamodb_tables()
        except:
            exit("Some error I did not catch.")

    def load_configuration(self):
        try:
            config_str = open(os.path.dirname(os.path.abspath(__file__)) + '/config.yml', 'r')
            self.config = yaml.load(config_str)
            logfile = os.path.dirname(os.path.abspath(__file__)) + "/" + self.config['general']['logfile']
            logging.basicConfig(filename=logfile, level=logging.INFO)
        except IOError as error:
            exit("Could not load config.yml: " + str(error))
        except:
            raise
            exit("Unexpected error:" + str(sys.exc_info()[0]))

    def create_dynamodb_tables(self):
        self.set_schema()
        pass

    def set_schema(self):
        billing_table_schema = self.conn.create_schema(
            hash_key_name='forum_name',
            hash_key_proto_value=str,
            range_key_name='subject',
            range_key_proto_value=str
        )
        pass

if __name__ == "__main__":
    cs = AWSBillingTODynamoDB()