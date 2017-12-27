#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:02:57 2017

@author: root
"""

from ctypes import *

class barley_amount(Union):
    _fields_ = [
            ("barley_long", c_long),
            ("barley_int", c_int),
            ("barley_char" , c_char * 8),
            ]
    
value = raw_input("Enter amount of barley to put into the vat:")
my_barley = barley_amount(int(value))
print "Barley amount as long : %ld" % my_barley.barley_long
print "Barley amount as an int: %d" % my_barley.barley_int
print "Barley amount as char : %s" % my_barley.barley_char