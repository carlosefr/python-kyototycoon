#!/usr/bin/env python
#
# Copyright 2011, Toru Maesaka
#
# Redistribution and use of this source code is licensed under
# the BSD license. See COPYING file for license description.

import config
import unittest
from kyototycoon import KyotoTycoon, KyotoTycoonException

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.kt_handle = KyotoTycoon()
        self.kt_handle.open(port=11978)
        self.LARGE_KEY_LEN = 8000

    def tearDown(self):
        self.kt_handle.close()

    def test_increment(self):
        self.assertTrue(self.kt_handle.clear())

        key = 'incrkey'
        self.assertEqual(self.kt_handle.increment(key, 10), 10)
        self.assertEqual(self.kt_handle.increment(key, 10), 20)
        self.assertEqual(self.kt_handle.increment(key, 10), 30)
        self.assertEqual(self.kt_handle.increment(key, 10), 40)
        self.assertEqual(self.kt_handle.increment(key, 10), 50)

        # Incrementing against a non numeric value. Must fail.
        self.assertTrue(self.kt_handle.set(key, 'foo'))
        self.assertRaises(KyotoTycoonException, self.kt_handle.increment, key, 10)

    def test_increment_double(self):
        self.assertTrue(self.kt_handle.clear())

        key = 'incrkey'
        self.assertEqual(self.kt_handle.increment_double(key, 1.23), 1.23)
        self.assertEqual(self.kt_handle.increment_double(key, 1.11), 2.34)
        self.assertEqual(self.kt_handle.increment_double(key, 0.16), 2.50)

if __name__ == '__main__':
    unittest.main()
