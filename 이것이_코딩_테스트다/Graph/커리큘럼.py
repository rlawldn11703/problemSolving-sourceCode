from collections import deque
import copy
N = int(input())
indegree,times = [[0,[]] for _ in range(N+1)],[0]*(N+1)
for i in range(1,N+1):
    info = list(map(int,input().split()))
    times[i] = info[0]
    indegree[i][0] = len(info[1:-1])
    for j in info[1:-1]:
        indegree[j][1].append(i)
q = deque([])
for i in range(1,N+1):
    if indegree[i][0] == 0:
        q.append(i)
ans = copy.deepcopy(times)
while q:
    x = q.popleft()
    for i in indegree[x][1]:
        ans[i] = max(ans[i],ans[x]+times[i])
        indegree[i][0] -= 1
        if indegree[i][0]==0:
            q.append(i)
[print(ans[i]) for i in range(1,N+1)]
