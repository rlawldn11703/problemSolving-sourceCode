N = int(input())
fear = list(map(int,input().split()))
fear.sort()
# 공포도가 적은 모험가부터 데려가야 최대한 많은 그룹
ans,cnt = 0,0
for f in fear:
    cnt += 1
    if cnt >= f:
        ans += 1
        cnt = 0
print(ans)
