#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   col_multi.py
@Time    :   2022/05/08 02:02:48
'''


from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy
from .multi_rid import MultiRid
import logging


class ColMulti(BaseStrategy):
    STRATEGYNAME = "ColMulti"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        BaseStrategy.solve(que)
        for col in range(SudokuQuestion.WIDTH):
            logging.debug("Processing Col: %d" % (col))
            tep = []
            for row in range(SudokuQuestion.HEIGHT):
                tep.append(que[row][col])
            MultiRid.multirid(tep)
        return que
