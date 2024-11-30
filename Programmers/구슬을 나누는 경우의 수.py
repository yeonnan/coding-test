import math

def solution(balls, share):
    return math.comb(balls, share)

# comb : 조합을 계산할 때 사용된다. (조합 : 특정 개수의 원수를 순서와 상관없이 선택하는 경우의 수 계산)
# math.comb : 주어진 두 정수 n과 k에 대해 n개의 아이템 중 k개를 선택하는 조합의 수 반환


