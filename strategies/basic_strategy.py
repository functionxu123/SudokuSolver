#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   basic_strategy.py
@Time    :   2022/05/06 23:35:44
'''

from common.sudoku_question import SudokuQuestion
import logging


class BaseStrategy:
    STRATEGYNAME = "BaseStrategy"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        if not isinstance(que, SudokuQuestion):
            logging.error("strategy input arg must be SudokuQuestion type")
            raise Exception("strategy input arg must be SudokuQuestion type")
