import math
n,k = map(int,input().split())
count = [[0]*2 for _ in range(7)]
for _ in range(n):
    sex,grade = map(int,input().split())
    count[grade][sex] += 1
ans = 0
for grade in range(1,7):
    for sex in range(2):
        ans += math.ceil(count[grade][sex]/k)
print(ans)


