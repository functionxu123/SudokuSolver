#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   col_unique.py
@Time    :   2022/05/06 23:34:05
'''

from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy
import logging


class RowUnique(BaseStrategy):
    STRATEGYNAME = "RowUnique"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        BaseStrategy.solve(que)
        for row in range(SudokuQuestion.HEIGHT):
            for col in range(SudokuQuestion.WIDTH):
                if que[row][col].isdefinite():
                    rid_num = que[row][col].get_minnum()
                    for rid_col in range(SudokuQuestion.WIDTH):
                        if rid_col == col:
                            continue
                        definite_before = que[row][rid_col].isdefinite()
                        que[row][rid_col].remove_num(rid_num)
                        definite_after = que[row][rid_col].isdefinite()
                        if not definite_before and definite_after:
                            logging.debug("[x=%d, y=%d] New Definite Digit To Be %d" % (
                                rid_col, row, que[row][rid_col].get_minnum()))
        return que
