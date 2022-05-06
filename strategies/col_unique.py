#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   col_unique.py
@Time    :   2022/05/06 23:34:05
'''

from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy


class ColUnique(BaseStrategy):
    @staticmethod
    def solve(que) -> SudokuQuestion:
        super().solve(que)
        for col in range(SudokuQuestion.WIDTH):
            unique_nums = []
            for row in range(SudokuQuestion.HEIGHT):
                if que[row][col].isdefinite():
                    rid_num=que[row][col].get_minnum()
                    for rid_row in range(SudokuQuestion.HEIGHT):
                        if rid_row == row: continue
                        que[rid_row][col].remove_num(rid_num)
        return que
