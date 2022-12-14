N,M = map(int,input().split())
balls = [0]*(M+1)
for wgt in list(map(int,input().split())):
    balls[wgt] += 1
ans = 0
for wgt in range(1,M+1):
    ans += balls[wgt]*(sum(balls)-balls[wgt])
print(ans//2)
