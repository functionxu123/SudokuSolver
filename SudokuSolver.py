#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SudokuSolver.py
@Time    :   2022/05/06 22:21:07
'''


from common.digit import Digit
import argparse
import datetime

parser = argparse.ArgumentParser(description='SudokuSolver parser')
parser.add_argument('-f',
                    "--filename",
                    type=str,
                    default="",
                    help='json file describe the Sudoku question')
parser.add_argument('-v',
                    "--verbose",
                    action="store_true",
                    default=False,
                    help='show every step detail')
parser.add_argument("-d", "--debug", action="store_true",
                    default=False, help="open debug mode")

args = parser.parse_args()


def DATESTAMPS(): return datetime.datetime.now().strftime(
    '%Y-%m-%d_%H:%M:%S.%f')  # 含微秒的日期时间2018-09-06_21:54:46.205213


class SudokuSolver:
    def __init__(self) -> None:
        pass

    def solve(self, question):
        pass
