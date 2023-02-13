from os import *
from sys import *
from collections import *
from math import *
def armstrong(n):
    size = len(str(n))
    sum = 0
    final_num = n
    for i in range(size):
        num = n%10
        sum = sum + num**size
        n = n // 10
    if sum == final_num:
        return True
    else:
        return False

n = int(input())
print(armstrong(n))
