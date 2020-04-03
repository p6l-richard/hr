#!/bin/python3

import os
import sys

inp = '12:05:45AM'

def timeConversion(s):
    s.strip()
    is_pm = True if inp[-2:].lower() == 'pm' else False
    hh_mm_ss_int_list = list(map(int, inp[:-2].split(':')))
    if is_pm and hh_mm_ss_int_list[0] < 12:
        hh_mm_ss_int_list[0] += 12
    elif not is_pm:
        hh_mm_ss_int_list[0] -= 12 if hh_mm_ss_int_list[0] == 12 else 0

    hh_mm_ss_str_list = list(map(lambda el: f"{el:02d}", hh_mm_ss_int_list))
    print(':'.join(hh_mm_ss_str_list))
    
timeConversion(inp)