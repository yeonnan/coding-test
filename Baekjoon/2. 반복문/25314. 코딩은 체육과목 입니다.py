# long int = 4
# long long int = 8
# long long long int = 12
# long long long long int = 16

N = int(input())

for _ in range(N//4):
    # end=' '는 출력 후 줄바꿈 대신 공백을 추가함
    # 출력 후 기본적으로 줄바꿈을 하지 않고, 자동 줄바꿈 대신 빈 문자열을 출력하게 하는 설정
    print('long', end = '')