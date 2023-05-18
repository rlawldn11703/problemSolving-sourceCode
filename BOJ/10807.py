n = int(input())
arr = list(map(int,input().split()))
count = [0] * 201
v = int(input())
for i in range(n):
    count[arr[i]+100] += 1
print(count[v+100])
