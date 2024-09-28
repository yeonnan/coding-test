n = int(input())    # 과목 수
score = list(map(int, input().split())) # 성적 리스트
m = max(score)  # 최고점

score_list = [] 
for i in score:  
    score_list.append(i/m*100)  # 각 성적을 최고점으로 나누고 100을 곱해 조정한 값을 리스트에 추가

avg = sum(score_list)/n    # 평균 점수
print(avg)