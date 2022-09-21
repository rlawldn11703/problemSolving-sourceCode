n,m = map(int,input().split())
ans = 0
for _ in range(n):
    l_min = min(list(map(int,input().split())))
    ans = max(ans,l_min)
print(ans)
