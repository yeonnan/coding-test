num = []

for i in range(9):
    a = int(input())
    num.append(a)

print(max(num))
print(num.index(max(num))+1)  # 리스트의 가장 큰 수를 출력하고 그 수의 인덱스 번호에 1추가