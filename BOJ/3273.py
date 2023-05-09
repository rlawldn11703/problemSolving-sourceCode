# 입력받기
n = int(input())
arr = list(map(int,input().split()))
x = int(input())
# 더해서 x를 만족하는 숫자쌍 dict로 저장
num_dict = {}
answer = 0
for num_1 in arr:
    num_2 = x-num_1
    if num_2 > 0 and num_2 in num_dict:
        answer += 1
    num_dict[num_1] = 1
        
print(answer)
