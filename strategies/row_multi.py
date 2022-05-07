#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   row_multi.py
@Time    :   2022/05/07 19:51:49
'''

from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy
import logging


class RowMulti(BaseStrategy):
    STRATEGYNAME = "RowMulti"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        BaseStrategy.solve(que)
        
        return que
