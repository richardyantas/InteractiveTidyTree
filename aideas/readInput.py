
'''
A repository consisting of Competitive Programming Problems and their solutions in Python Programming Language.
Python input output
ex: name =input()
ex: print('Hello {0}'.format(name))

Examples
ex: Get the input for the two variables num1, num2 = map(int, input().split())
ex: Get a list of numbers as input list(map(int, input().split()))
ex: Sum sum_numbers = sum(num_array)
ex: Range for i in range(start, stop [, step] ): pass
ex: Adding the corresponding elements of two lists Method 1 res_list = [test_list1[i] + test_list2[i] for i in range(len(test_list1))]
Method 2 from operator import add res_list = list(map(add, test_list1, test_list2))
Method3 res_list = list(map(lambda x, y : x + y, test_list1, test_list2))
import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br
sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))
ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1
flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))
mod=1000000007
#main code

import sys
input = sys.stdin.readline

def inp():
    return (int(input))

def inlt():
    return (list(map(int,input().split())))

def insr():
    s = input()
    return (list(s[:len(s)-1]))

def invr():
    return map(int,input().split())

'''

#a, b, c, d = [int(x) for x in input().split()]
#print(a*b*c*d)

#a, b, c, d = map(int, input().split())
#print(a*b*c*d)

n = str(input())
l = [str(x) for x in input().split()]
print(l)


# https://algocoding.wordpress.com/2015/02/18/how-to-read-input-in-python-in-codeforces/


n = int(input())
for i in range(n):
    a, m = map(int, input().split())
    lst = list(map(int, input().split()))


import sys
for line in sys.stdin:
    numbers = [int(x) for x in line.strip().split()]
    print(numbers)

# https://codeforces.com/blog/entry/71884