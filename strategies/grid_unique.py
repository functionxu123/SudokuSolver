#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   col_unique.py
@Time    :   2022/05/06 23:34:05
'''

from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy


class GridUnique(BaseStrategy):
    GRID_WIDTH = 3
    GRID_HEIGHT = 3

    @staticmethod
    def solve(que) -> SudokuQuestion:
        super().solve(que)
        for grow in range(SudokuQuestion.HEIGHT/GridUnique.GRID_HEIGHT):
            for gcol in range(SudokuQuestion.WIDTH/GridUnique.GRID_WIDTH):

                for drow in range(grow*GridUnique.GRID_HEIGHT, (grow+1)*GridUnique.GRID_HEIGHT):
                    for dcol in range(gcol*GridUnique.GRID_WIDTH, (gcol+1)*GridUnique.GRID_WIDTH):
                        if que[drow][dcol].isdefinite():
                            rid_num = que[drow][dcol].get_minnum()
                            for rid_drow in range(grow*GridUnique.GRID_HEIGHT, (grow+1)*GridUnique.GRID_HEIGHT):
                                for rid_dcol in range(gcol*GridUnique.GRID_WIDTH, (gcol+1)*GridUnique.GRID_WIDTH):
                                    if rid_drow == drow and rid_dcol == dcol:
                                        continue
                                    que[rid_drow][rid_dcol].remove_num(rid_num)
        return que
