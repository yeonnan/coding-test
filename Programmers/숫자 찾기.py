def solution(num, k):
    num = str(num)
    k = str(k)
    if k in num:
        answer = num.index(k)+1
    else: 
        answer = -1
    return answer