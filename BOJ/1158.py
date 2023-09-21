n,k = map(int,input().split())
linked_list = dict()
for i in range(1,n+1):
    linked_list[i] = [i-1,i+1]
linked_list[1][0] = n
linked_list[n][1] = 1
perm = []
node = 1
while linked_list:
    for _ in range(k-1):
        node = linked_list[node][1]
    # node의 앞,뒤를 연결
    perm.append(node)
    prev,next = linked_list[node]
    linked_list[prev][1] = next
    linked_list[next][0] = prev
    del linked_list[node]
    node = next
ans = '<'+', '.join(map(str,perm))+'>'
print(ans)

# ans
n,k = map(int,input().split())
prev,next = [0]*5001,[0]*5001
v = []
for i in range(1,n+1):
    prev[i] = i-1 if i != 1 else n
    next[i] = i+1 if i != n else 1
i,cur = 1,1     
while n > 0:
    if i == k:
        prev[next[cur]] = prev[cur] 
        next[prev[cur]] = next[cur]
        v.append(cur)
        i = 1
        n -= 1
    else:
        i += 1
    cur = next[cur]
ans = '<'+', '.join(map(str,v))+'>'
print(ans)
