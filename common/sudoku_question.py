#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sudoku_question.py
@Time    :   2022/05/06 22:37:22
'''

from .positive_digit import PosDigit
import json
import logging


class SudokuQuestion:
    WIDTH = 9
    HEIGHT = 9

    def __init__(self, jsonpath) -> None:
        tep_question = []
        with open(jsonpath, "r") as f:
            tep_question = json.load(f)

        if not isinstance(tep_question, list) or len(tep_question) != self.HEIGHT:
            logging.error("Loading json file error: json formate error")
            raise Exception("Loading json file error")
        self.__question = []
        for row in tep_question:
            tep_que = []
            for col in row:
                if not col or col == "*":
                    tep_que.append(PosDigit())
                else:
                    dig = int(col)
                    tep_que.append(PosDigit(dig))
            if len(tep_que) != self.WIDTH:
                logging.error("Loading json file error: json formate error")
                raise Exception("Loading json file error")
            self.__question.append(tep_que)

    def __getitem__(self, index):
        return self.__question[index]

    def __setitem__(self, key, value):
        self.__question[key] = value

    def show(self):
        for row in self.__question:
            print("|", end="")
            for col in row:
                col.show()
                print("|", end="")
            print()

    def get_desc(self):
        ret = ""
        for row in self.__question:
            ret += "|"
            for col in row:
                ret += col.get_desc()
                ret += "|"
            ret += "\n"
        return ret

    def get_entropy(self):
        ret = 0
        for row in self.__question:
            for col in row:
                ret += col.get_entropy()
        return ret

    def isdefinite(self):
        for row in self.__question:
            for col in row:
                if not col.isdefinite():
                    return False
        return True

    def check(self):
        for indr, row in enumerate(self.__question):
            for indc, col in enumerate(row):
                if not col.check():
                    self.show()
                    logging.error("Digit error at: x=%d, y=%d " % (indc, indr))
                    return False
        return True

    def get_firstindefinite(self):
        for indr, row in enumerate(self.__question):
            for indc, col in enumerate(row):
                if not col.isdefinite():
                    return indr, indc
        return None, None
