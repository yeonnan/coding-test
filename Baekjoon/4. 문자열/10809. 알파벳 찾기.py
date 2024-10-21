s = input()
# for i in 'abcdefghijklmnopqrstuvwxyz':
#     print(s.find(i), end=' ')

char = 'abcdefghijklmnopqrstuvwxyz'
for i in char:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')