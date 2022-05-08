#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   multi_rid.py
@Time    :   2022/05/08 00:38:51
'''

from common import digit
import logging


class MultiRid:
    @staticmethod
    def listdigit_or(digits):
        if len(digits) <= 0:
            return None
        ret = digits[0]
        for i in digits:
            ret = ret | i
        return ret

    @staticmethod
    def multirid(digits):
        if not isinstance(digits, list):
            logging.error("multirid accepts only list of digits")
            raise Exception("multirid accepts only list of digits")
        if len(digits) <= 0:
            return
        if not isinstance(digits[0], digit.Digit):
            logging.error("multirid accepts only list of digits")
            raise Exception("multirid accepts only list of digits")
        # do multi rid init
        count_index = {}
        for ind, dig in enumerate(digits):
            cnt = dig.get_count()
            if cnt <= 1:
                continue
            if cnt not in count_index:
                count_index[cnt] = []
            count_index[cnt].append([ind])
        # iter to find mult but unique
        len_no_difinite = sum([(0 if x.isdefinite() else 1) for x in digits])
        max_count = min(len(digits[0]), len_no_difinite-1)
        for cnt in range(2, max_count):
            if cnt not in count_index:
                continue

            for indi, i in enumerate(count_index[cnt]):
                # judge if this cnt has unique
                if len(i) > cnt:
                    logging.error("Multirid solving question invalid")
                    raise Exception("question invalid")
                elif len(i) == cnt:
                    # do rid
                    tep_dig = MultiRid.listdigit_or([digits[x] for x in i])
                    logging.debug("Get one multirid [count: %d, rid nums: %s , formate indexs: %s]" % (
                        cnt, str(tep_dig.get_allnum()), str(i)))
                    for ti in range(len(digits)):
                        if ti in i or digits[ti].isdefinite():
                            continue
                        definite_before = digits[ti].isdefinite()
                        digits[ti] &= (~tep_dig)
                        definite_after = digits[ti].isdefinite()

                        if not digits[ti].check():
                            logging.error(
                                "After rid %s index %d digit invalid, rid digit index: %s" % (str(tep_dig.get_allnum()), ti, str(i)))
                            raise Exception("Digit don't have valid num")

                        if not definite_before and definite_after:
                            logging.debug("[index=%d] New Definite Digit To Be %d" % (
                                ti, digits[ti].get_minnum()))
                    continue

                for indj, j in enumerate(count_index[cnt]):
                    if indj <= indi:
                        continue

                    tep_indexlist = list(set(i+j))
                    # one contains another
                    if len(tep_indexlist) == len(i) or len(tep_indexlist) == len(j):
                        continue

                    tep_dig = MultiRid.listdigit_or(
                        [digits[x] for x in tep_indexlist])
                    tep_cnt = tep_dig.get_count()
                    if tep_cnt not in count_index:
                        count_index[tep_cnt] = []

                    if tep_indexlist not in count_index[tep_cnt] and tep_cnt < len_no_difinite:
                        count_index[tep_cnt].append(tep_indexlist)
                        logging.debug("Count %d add one item: %s which means nums: %s" %
                                      (tep_cnt, str(tep_indexlist), str(tep_dig.get_allnum())))
