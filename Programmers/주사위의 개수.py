def solution(box, n):
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    return a * b * c

box = list(map(int, input().split()))
n = int(input())
print(solution(box,n))