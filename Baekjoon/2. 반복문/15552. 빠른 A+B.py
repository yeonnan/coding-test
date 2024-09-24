import sys 

i = int(sys.stdin.readline())

for _ in range(i):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)