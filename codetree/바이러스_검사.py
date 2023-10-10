import math
n = int(input())
clients = list(map(int,input().split()))
leader,member = map(int,input().split())
def count_inspector(client):
    # client : 검사해야할 고객수
    cnt = 1 # 팀장은 무조건 있어야 해!
    if leader >= client: # 팀장이 다 처리 가능하다면 
        return cnt
    # 불가능하다면 처리하고 남은 고객수 팀원이 처리
    client -= leader
    cnt += math.ceil(client/member)
    return cnt
ans = 0
for client in clients:
    ans += count_inspector(client)
print(ans)
