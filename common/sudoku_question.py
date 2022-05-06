#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sudoku_question.py
@Time    :   2022/05/06 22:37:22
'''

from .digit import Digit
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
        self.question = []
        for row in tep_question:
            tep_que = []
            for col in row:
                if col == "*":
                    tep_que.append(Digit())
                else:
                    dig = int(col)
                    tep_que.append(Digit(dig))
            if len(tep_que) != self.WIDTH:
                logging.error("Loading json file error: json formate error")
                raise Exception("Loading json file error")
            self.question.append(tep_que)

    def __getitem__(self, index):
        return self.question[index]

    def __setitem__(self, key, value):
        self.question[key] = value
