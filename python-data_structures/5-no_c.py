#!/usr/bin/python3
def no_c(my_string):
    new_string = ''.join(
        char for char in my_string if char != 'c' and char != 'C'
    )
    return new_string
