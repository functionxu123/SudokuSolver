#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   row_multi.py
@Time    :   2022/05/07 19:51:49
'''

from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy
from .multi_rid import MultiRid
import logging


class RowMulti(BaseStrategy):
    STRATEGYNAME = "RowMulti"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        BaseStrategy.solve(que)
        for row in range(SudokuQuestion.HEIGHT):
            logging.debug("Processing Row: %d" % (row))
            tep = []
            for col in range(SudokuQuestion.WIDTH):
                tep.append(que[row][col])
            MultiRid.multirid(tep)
        return que
