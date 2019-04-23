#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

with sys.stdin as csvfile:
    csv_rd = csv.reader(csvfile, delimiter =',')
    csv_rd.next()
    for dataline in csv_rd:
        dataline = dataline[-5:]
        dataline = filter(None, dataline)
        for lineitems in dataline:
            print '%s\t%s' % (lineitems,1)
