N = int(input())
arr = list(map(int,input().split()))
ans = [-1] * N
stack = []
for i in range(N):
    num = arr[i]
    while stack and num > stack[-1][0]:
        idx = stack.pop()[1]
        ans[idx] = num
    stack.append((num,i))
print(*ans)

# answer
n = int(input())
a = list(map(int, input().split()))
ans = [-1] * n
S = []
for i in range(n - 1, -1, -1):
    while S and S[-1] <= a[i]:
        S.pop()
    if not S:
        ans[i] = -1
    else:
        ans[i] = S[-1]
    S.append(a[i])
print(*ans)
