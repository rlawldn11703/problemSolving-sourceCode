import sys
N = int(sys.stdin.readline())
ropes = []
for _ in range(N):
    rope = int(sys.stdin.readline())
    ropes.append(rope)
ropes.sort(reverse=True)
ans = ropes[0]
for i in range(1,N):
    ans = max(ans,ropes[i] * (i+1))
print(ans)

# answer
n = int(input())
w = []
for _ in range(n):
    rope = int(sys.stdin.readline())
    w.append(rope)
w.sort()
ans = 0
for i in range(1, n+1):
    ans = max(ans, w[n-i]*i)
print(ans)
