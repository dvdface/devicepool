#!/usr/bin/python
# -*- coding: UTF-8 -*-

from unittest import TestCase

from devicepool import DevicePool



class TestDeviePool(TestCase):

    def test_get_and_free(self):
        pool = DevicePool([{'id':1}, {'id':2}])
        dev1 = pool.get()
        dev2 = pool.get()
        dev3 = pool.get()

        self.assertTrue(dev1.id == 1)
        self.assertTrue(dev2.id == 2)
        self.assertTrue(dev3 == None)

        del dev1
        dev4 = pool.get()
        self.assertTrue(dev4.id == 1)
        dev5 = pool.get()
        self.assertTrue(dev5 == None)

        del dev2
        dev6 = pool.get()
        self.assertTrue(dev6.id == 2)


    def test_filter(self):
        pool = DevicePool([{'id':1}, {'id':2}])
        dev1 = pool.get(filter_func=lambda dev: dev.id == 2)
        self.assertTrue(dev1.id == 2)
        del dev1

        dev2 = pool.get(filter_func=lambda dev: dev.id == 3)
        self.assertTrue(dev2 == None)
