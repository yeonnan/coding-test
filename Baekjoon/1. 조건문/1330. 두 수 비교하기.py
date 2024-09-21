A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')


'''
삼항연산자
조건식 1이 참일 때 값 if 조건식 1 else [ 조건식2가 참일 때 값 if 조건식2 else 조건식이 모두 거짓일 때 값 ]
'''

print('>') if A > B else print('<') if A < B else print('==')