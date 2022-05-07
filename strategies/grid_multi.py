#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   grid_multi.py
@Time    :   2022/05/08 02:04:44
'''


from common.sudoku_question import SudokuQuestion
from .basic_strategy import BaseStrategy
from .multi_rid import MultiRid
import logging


class GridMulti(BaseStrategy):
    GRID_WIDTH = 3
    GRID_HEIGHT = 3
    STRATEGYNAME = "GridMulti"

    @staticmethod
    def solve(que) -> SudokuQuestion:
        BaseStrategy.solve(que)
        for grow in range(int(SudokuQuestion.HEIGHT/GridMulti.GRID_HEIGHT)):
            for gcol in range(int(SudokuQuestion.WIDTH/GridMulti.GRID_WIDTH)):
                logging.debug("Processing Grid: [x=%d, y=%d]"%(gcol, grow))
                tep=[]
                for drow in range(grow*GridMulti.GRID_HEIGHT, (grow+1)*GridMulti.GRID_HEIGHT):
                    for dcol in range(gcol*GridMulti.GRID_WIDTH, (gcol+1)*GridMulti.GRID_WIDTH):
                        tep.append(que[drow][dcol])
                MultiRid.multirid(tep)
        return que
