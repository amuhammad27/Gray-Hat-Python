
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from ctypes import *

libc = CDLL("libc.so.6")
message_string = "Hello world! \n"
libc.printf("Testing: %s", message_string)
