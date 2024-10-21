while True :
    try :
        print(input())
    except EOFError:
        break

# EOFError : 파일에서 더이상 읽을 내용이 없거나 입력 값이 없을 때 발생하는 에러