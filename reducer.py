#!/usr/bin/env python
"""reducer.py"""

import sys

vehtype = None
acccount = 0
word = None

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if vehtype == word:
        acccount += count
    else:
        if vehtype:
            print '%s\t%s' % (vehtype, acccount)
        acccount = count
        vehtype = word

if vehtype == word:
    print '%s\t%s' % (vehtype, acccount)
