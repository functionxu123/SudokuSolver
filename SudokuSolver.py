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
import copy
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

    def step(self, que, strategys=STRATEGYS):
        entropy_change = 0
        for strategy in strategys:
            logging.info("USING STRATEGY: %s"% strategy.STRATEGYNAME)
            old_entropy = que.get_entropy()
            logging.info("BEFORE: [ENTROPY= %f ]"%old_entropy)
            que.show()
            strategy.solve(que)
            new_entropy = que.get_entropy()
            logging.info("AFTER: [ENTROPY= %f CHANGE: %f ]"%(new_entropy, old_entropy-new_entropy))
            que.show()
            entropy_change += old_entropy-new_entropy
            if new_entropy==0:
                logging.info("All Digits Resolved, This Question Is Done")
                break
        if entropy_change==0 and que.get_entropy()!=0 and strategys==STRATEGYS:
            entropy_change+=self.step(que, STRATEGYS_HEAVY)
        return entropy_change
    
    def get_multi_answer(self, que):
        ret=[]
        if que.isdefinite():
            ret.append(que.get_desc())
        else:
            row, col = que.get_firstindefinite()
            iternums=que[row][col].get_allnum()
 
            for ind,num in enumerate(iternums):
                tep_que=copy.deepcopy(que)
                tep_que[row][col].set_only_num(num)
                logging.info("ASSUME DIGIT[x=%d, y=%d] TO BE %d, TRY NEW SOLVE: %d/%d"%(col, row, num, ind+1, len(iternums)))
                try:
                    ret+=self.solve(tep_que)
                except Exception as e:
                    logging.info("THIS WAY IS WRONG\n")
                    continue
        return ret
    
    def solve(self, que):
        step_index=0
        while que.get_entropy()!=0:
            logging.info("STEP [%d]"%step_index)
            ret=self.step(que, STRATEGYS)
            step_index+=1

            if not ret:
                break
        return self.get_multi_answer(que)


    def solveall(self):
        ansers=self.solve(self.question)
        
        logging.info ("FINALLY GET ANSWERS TOTAL: %d"%len(ansers))
        for ind,i in enumerate(ansers):
            logging.info("ANSWER %d: \n%s"%(ind, i))

if __name__=="__main__":
    tep = SudokuSolver(args)
    tep.solveall()
    