#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015 Monk-ee (magic.monkee.magic@gmail.com).
#

"""__init__.py: Init for unit testing this module."""

__author__ = "monkee"
__maintainer__ = "monk-ee"
__email__ = "magic.monkee.magic@gmail.com"
__status__ = "Development"

import unittest

from PuppetDBClientTestCaseV2 import PuppetDBClientTestCaseV2
from PuppetDBClientTestCaseV3 import PuppetDBClientTestCaseV3


def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PuppetDBClientTestCaseV2))
    suite.addTest(unittest.makeSuite(PuppetDBClientTestCaseV3))
    return suite
