def solution(numbers, k):
    answer = 0
    for i in range(k-1):
        answer = (answer+2) % len(numbers)      # 2명 건너 뛰기
    # 공 받는 사람 번호
    return numbers[answer]

numbers = list(map(int, input().split()))
k = int(input())
print(solution(numbers, k))