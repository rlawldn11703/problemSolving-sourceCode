import sys
n,arr = int(input()),[]
for _ in range(n):
    name,score = sys.stdin.readline().split()
    arr.append((name,int(score)))
arr.sort(key=lambda x:x[1])
[print(i[0],end= ' ') for i in arr]
