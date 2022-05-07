#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   SudokuSolver.py
@Time    :   2022/05/06 22:21:07
'''


from common import sudoku_question
import argparse
import datetime
import logging
from strategies import col_unique, grid_unique, row_unique, row_multi, col_multi, grid_multi

parser = argparse.ArgumentParser(description='SudokuSolver parser')
parser.add_argument('-f',
                    "--filename",
                    type=str,
                    default="",
                    required=True,
                    help='json file describe the Sudoku question')
parser.add_argument("-d", "--debug", action="store_true",
                    default=False, help="open debug mode")

args = parser.parse_args()

# set logging level
logging_format = '%(asctime)s [%(levelname)s] %(message)s'
if args.debug:
    logging.basicConfig(level=logging.DEBUG, format=logging_format)
else:
    logging.basicConfig(level=logging.INFO, format=logging_format)


def DATESTAMPS(): return datetime.datetime.now().strftime(
    '%Y-%m-%d_%H:%M:%S.%f')  # 含微秒的日期时间2018-09-06_21:54:46.205213


STRATEGYS = [col_unique.ColUnique(), grid_unique.GridUnique(),
             row_unique.RowUnique()]

STRATEGYS_HEAVY = [row_multi.RowMulti(), col_multi.ColMulti(), grid_multi.GridMulti()]


class SudokuSolver:
    def __init__(self, args=args) -> None:
        self.args = args
        self.question = sudoku_question.SudokuQuestion(args.filename)

    def step(self, index=0, strategys=STRATEGYS):
        print("\n\nSTEP [", index, "]")
        entropy_change = 0
        for strategy in strategys:
            print("\nUSING STRATEGY: ", strategy.STRATEGYNAME)
            old_entropy = self.question.get_entropy()
            print("BEFORE: [ENTROPY=", old_entropy, "]")
            self.question.show()
            self.question = strategy.solve(self.question)
            new_entropy = self.question.get_entropy()
            print("AFTER: [ENTROPY=", new_entropy, " CHANGE: ",
                  old_entropy-new_entropy, "]")
            self.question.show()
            entropy_change += old_entropy-new_entropy
            if new_entropy==0:
                logging.info("all digits resolved, this question is done")
                break
        if entropy_change==0 and self.question.get_entropy()!=0 and strategys==STRATEGYS:
            entropy_change+=self.step(index, STRATEGYS_HEAVY)
        return entropy_change

    def solveall(self):
        step_index=0
        while self.question.get_entropy()!=0:
            ret=self.step(step_index)
            step_index+=1

            if not ret:
                break

if __name__=="__main__":
    tep = SudokuSolver(args)
    tep.solveall()
    