from math import factorial

def solution(n):
    for i in range(1, 12):
        if n < factorial(i):
            return i - 1
