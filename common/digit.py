#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Digit.py
@Time    :   2022/05/06 21:38:43
'''
import logging


class Digit:
    LIMIT_MAX = 9
    LIMIT_MIN = 0

    def __init__(self, initnum=None) -> None:
        length = self.LIMIT_MAX - self.LIMIT_MIN + 1
        self.__num = [1]*length
        if isinstance(initnum, list):
            self.__num = [0]*length
            for i in initnum:
                if i > self.LIMIT_MAX or i < self.LIMIT_MIN:
                    logging.error("Setting invalid num to digit")
                    continue
                self.__num[i] = 1
        elif isinstance(initnum, int):
            self.__num = [0]*10
            if i > self.LIMIT_MAX or i < self.LIMIT_MIN:
                logging.error("Setting invalid num to digit")
                return
            self.__num[initnum] = 1

    def add_num(self, num):
        if num > self.LIMIT_MAX or num < self.LIMIT_MIN:
            logging.error("Adding invalid num to digit")
            return None
        self.__num[num] = 1
        return True

    def remove_num(self, num):
        if num > self.LIMIT_MAX or num < self.LIMIT_MIN:
            logging.error("Removing invalid num on digit")
            return None
        self.__num[num] = 0
        return True

    def isdefinite(self):
        return sum(self.__num) == 1

    def __len__(self):
        return self.LIMIT_MAX - self.LIMIT_MIN + 1
