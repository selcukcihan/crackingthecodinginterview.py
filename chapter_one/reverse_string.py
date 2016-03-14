#! /usr/bin/env python
"""
"""

def reverse_string(input_string):
    """ Converts the string to array of chars to emulate c-style strings."""
    if not input_string[-1] == '\0':
        raise Exception("Input string should end with null character.")
    str_array = list(input_string[:-1])
    for i, c in enumerate(str_array[:len(input_string) / 2]):
        tmp = str_array[i]
        str_array[i] = str_array[-(i + 1)]
        str_array[-(i + 1)] = tmp
    str_array.append('\0')
    return "".join(str_array)
        
