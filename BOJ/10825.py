import sys
n = int(input())
data = []
for _ in range(n):
    data.append(sys.stdin.readline().split())
data.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
[print(x[0]) for x in data]
