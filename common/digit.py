#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Digit.py
@Time    :   2022/05/06 21:38:43
'''
import logging
import math
import copy


class Digit(object):
    LIMIT_MAX = 9
    LIMIT_MIN = 0

    def __init__(self, initnum=None) -> None:
        length = self.__len__()
        self.__num = [1]*length
        if isinstance(initnum, list):
            self.__num = [0]*length
            for i in initnum:
                if i > self.LIMIT_MAX or i < self.LIMIT_MIN:
                    logging.error("Setting invalid num to digit")
                    continue
                self.__num[i-self.LIMIT_MIN] = 1
        elif isinstance(initnum, int):
            self.__num = [0]*length
            if initnum > self.LIMIT_MAX or initnum < self.LIMIT_MIN:
                logging.error("Setting invalid num to digit")
                return
            self.__num[initnum-self.LIMIT_MIN] = 1

    def add_num(self, num):
        return self.set_num(num, 1)

    def remove_num(self, num):
        return self.set_num(num, 0)

    def set_num(self, num, val):
        if num > self.LIMIT_MAX or num < self.LIMIT_MIN:
            logging.error("Setting invalid num on digit: %d over [%d, %d]" % (
                num, self.LIMIT_MIN, self.LIMIT_MAX))
            return None
        self.__num[num-self.LIMIT_MIN] = (1 if val else 0)
        return True

    def has_num(self, num):
        if num > self.LIMIT_MAX or num < self.LIMIT_MIN:
            return False
        return self.__num[num-self.LIMIT_MIN]

    def isdefinite(self):
        return sum(self.__num) == 1

    def get_minnum(self):
        for ind, i in enumerate(self.__num):
            if i:
                return ind + self.LIMIT_MIN
        return None

    def get_maxnum(self):
        ret = None
        for ind, i in enumerate(self.__num):
            if i:
                ret = ind + self.LIMIT_MIN
        return ret

    def __len__(self):
        return self.LIMIT_MAX - self.LIMIT_MIN + 1

    def __and__(self, obj):
        if not isinstance(obj, Digit):
            raise Exception("Digit operator '&' rvalue is not a Digit")
        if self.LIMIT_MAX != obj.LIMIT_MAX or self.LIMIT_MIN != obj.LIMIT_MIN:
            raise Exception(
                "Digit operator '&' lvalue and rvalue is not same Digit")
        ret = copy.copy(self)
        for ind, i in enumerate(obj.__num):
            ret.__num[ind] &= i
        return ret

    def __or__(self, obj):
        if not isinstance(obj, Digit):
            raise Exception("Digit operator '|' rvalue is not a Digit")
        if self.LIMIT_MAX != obj.LIMIT_MAX or self.LIMIT_MIN != obj.LIMIT_MIN:
            raise Exception(
                "Digit operator '|' lvalue and rvalue is not same Digit")
        ret = copy.copy(self)
        for ind, i in enumerate(obj.__num):
            ret.__num[ind] |= i
        return ret

    def __xor__(self, obj):
        if not isinstance(obj, Digit):
            raise Exception("Digit operator '^' rvalue is not a Digit")
        if self.LIMIT_MAX != obj.LIMIT_MAX or self.LIMIT_MIN != obj.LIMIT_MIN:
            raise Exception(
                "Digit operator '^' lvalue and rvalue is not same Digit")
        ret = copy.copy(self)
        for ind, i in enumerate(obj.__num):
            ret.__num[ind] ^= i
        return ret

    def show(self):
        if self.isdefinite():
            print(self.get_minnum(), end="")
        else:
            print("*", end="")

    def get_entropy(self):
        if not self.check():
            raise Exception("Digit don't have valid num")
        return math.log(sum(self.__num))

    def check(self):
        if sum(self.__num) <= 0:
            logging.error("digit check error: no valid num")
            return False
        return True
