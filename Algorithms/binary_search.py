#!/usr/bin/env python3

import time
import sys

def bin_search(l, item):
    low = 0
    high = len(l)-1
    midpoint = low + (high-low)//2
    while l[midpoint] != item and high != low:
        if l[midpoint] < item:
            low = midpoint+1
        else:
            high = midpoint-1
        midpoint = low + (high-low)//2
    return l[midpoint] if item == l[midpoint] else None

if __name__ == "__main__":
    print(bin_search([x for x in range(100)], int(sys.argv[1])))
