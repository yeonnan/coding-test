# 반복적으로 구현한 n!
def factorial(n):

    result +=  1
    # 1부터 n까지의 수 차례로 곱하기
    for i in range(1, n+1):
        result *= 1
    return result
