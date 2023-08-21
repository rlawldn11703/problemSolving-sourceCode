n = int(input())
tower = list(map(int,input().split()))
stack = [(100000001,0)]
ans = []
for i in range(1,n+1):
    while tower[i-1] > stack[-1][0] :
        stack.pop()
    ans.append(stack[-1][1])
    stack.append((tower[i-1],i))
print(*ans)
