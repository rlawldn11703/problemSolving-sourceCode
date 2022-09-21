n,k = map(int,input().split())
ans = 0
while n>1:
    if n >= k:
        ans += n%k
        n //= k
        ans += 1
    else:
        ans += n-1
        n = 1
print(ans)
