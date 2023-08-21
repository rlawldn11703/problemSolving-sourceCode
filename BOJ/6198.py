import sys
N = int(sys.stdin.readline())
stack, ans, heights = [(int(1e9),0)],0 ,[]
for _ in range(N):
    height = int(sys.stdin.readline())
    heights.append(height)
heights = heights[::-1]
for i in range(N): 
    cnt = 0
    while heights[i] > stack[-1][0]:
        d = stack.pop()[1] + 1
        cnt += d
    ans += cnt
    stack.append((heights[i],cnt))
print(ans)

# answer
n = int(input())
s = []
ans = 0
for _ in range(n):
    h = int(input())
    while s and s[-1] <= h:
        s.pop()
    ans += len(s)
    s.append(h)
print(ans)
