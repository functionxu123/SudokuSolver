#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   positive_digit.py
@Time    :   2022/05/06 23:24:37
'''

from .digit import Digit

class PosDigit(Digit):
    LIMIT_MAX = 9
    LIMIT_MIN = 1