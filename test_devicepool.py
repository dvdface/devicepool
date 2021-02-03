#!/usr/bin/python
# -*- coding: UTF-8 -*-

from unittest import TestCase

from devicepool import *
import time
import pytest



class TestDeviePool(TestCase):

    def test_basic(self):
        pool = DevicePool([{'id':1}, {'id':2}])
        dev1 = pool.get()
        dev2 = pool.get()

        self.assertTrue(dev1.id == 1)
        self.assertTrue(dev2.id == 2)

        dev1.free()
        dev3 = pool.get()
        self.assertTrue(dev3.id == 1)

        dev2.free()
        dev4 = pool.get()
        self.assertTrue(dev4.id == 2)
        dev3.free()
        dev4.free()

    def test_filter(self):
        pool = DevicePool([{'id':1}, {'id':2}])
        dev1 = pool.get(filter_func=lambda dev: dev.id == 2)
        self.assertTrue(dev1.id == 2)
        del dev1

        dev2 = pool.get(filter_func=lambda dev: dev.id == 3)
        self.assertTrue(dev2 == None)

    def test_readonly(self):

        pool = DevicePool([{'id':1}, {'id':2}])
        dev = pool.get()
        try:
            dev.id = 3
        except RuntimeError as re:
            assert True
            dev.free()
            return
        
        assert False
        
    def test_writtable(self):

        pool = DevicePool([{'id':1}])
        dev = pool.get()
        try:
            dev.x = 3
            dev.free()
            dev = pool.get()
            assert dev.x != 3 
        except AttributeError as ae:
            assert True
            dev.free()
            return
        
        assert False

    def test_size(self):
        pool = DevicePool([{'id':1}])
        assert pool.size == 1
        dev = pool.get()
        assert pool.size == 0
        dev.free()
        assert pool.size == 1
    
    def test_stress(self):
        pool = DevicePool([{'id':1}])
        for i in range(0, 10000):
            assert pool.size == 1
            dev = pool.get()
            assert pool.size == 0
            dev.free()
    
    def test_free(self):
        pool = DevicePool([{'id':1}])
        for i in range(0, 10000):
            assert pool.size == 1
            dev = pool.get()
            assert pool.size == 0
            dev.free()
            assert pool.size == 1


    def test_force_free(self):
        pool = DevicePool([{'id':1}])
        try:
            
            dev = pool.get(rent_time=3)
            assert pool.size == 0
            time.sleep(5)
        except TimeoutError as tme:
            assert pool.size == 1
