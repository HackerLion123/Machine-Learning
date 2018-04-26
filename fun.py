#!/bin/python

import sys

def getTotalX(a, b):
# Complete this function
    count = 0
    for i in range(max(a),min(b)+1):
        for j in range(0,len(a)):
            if i%a[j] == 0:
                aref = True
            else:
                aref = False
                break
        if(a):
            for k in range(0,len(b)):
                if b[k]%i == 0:
                    bref = True
                else:
                    bref = False
                    break
        if(aref == True and bref == True):
            count = count + 1
    return count

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total

