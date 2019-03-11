#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    reverse_string = input_string[::-1]
    #input_string_no_space = input_string.replace(' ', '')
    #reverse_string_no_space = reverse_string.replace(' ', '')

    if input_string.lower() == reverse_string.lower(): return True
    else: return False