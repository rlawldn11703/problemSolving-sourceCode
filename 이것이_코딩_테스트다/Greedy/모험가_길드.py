N = int(input())
fear = list(map(int,input().split()))
fear.sort()
print(fear)
# 공포도가 적은 모험가부터 데려가야 최대한 많은 그룹
ans,i = 0,0
while i < N:
    i += max(fear[i:i+fear[i]])
    if i>N:
        continue
    ans += 1
print(ans)
