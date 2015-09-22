# -*- coding: UTF-8 -*-
"""
    Simple app converts Celsius do Fahrenheit od F to C.
"""

def convert_temp(temp, base='C'):
    temp_f = temp * 1.8 + 32
    temp_c = (temp - 32) / 1.8

    if base == 'C':
        return temp_f
    else:
        return temp_c

print convert_temp(25)
print convert_temp(25, 'F')
