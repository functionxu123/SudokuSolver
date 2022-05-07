#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   col_unique.py
@Time    :   2022/05/06 23:34:05
'''

from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy
import logging


class ColUnique(BaseStrategy):
    STRATEGYNAME = "ColUnique"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        BaseStrategy.solve(que)
        for col in range(SudokuQuestion.WIDTH):
            for row in range(SudokuQuestion.HEIGHT):
                if que[row][col].isdefinite():
                    rid_num = que[row][col].get_minnum()
                    for rid_row in range(SudokuQuestion.HEIGHT):
                        if rid_row == row:
                            continue
                        definite_before = que[rid_row][col].isdefinite()
                        que[rid_row][col].remove_num(rid_num)
                        definite_after = que[rid_row][col].isdefinite()
                        if not definite_before and definite_after:
                            logging.debug("[x=%d, y=%d] New Definite Digit To Be %d" % (
                                col, rid_row, que[rid_row][col].get_minnum()))
        return que
