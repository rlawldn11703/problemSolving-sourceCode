# N개의 정수로 이루어진 수열에서 두 수를 골랐을 때,
# 그 차이가 M 이상이면서 제일 작은 경우
import sys
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort() # O(nlogn) 시간 소요
s,e = 0,0
ans = sys.maxsize
while s<= e and e < n:
    diff = arr[e]-arr[s]
    if diff >= m:
        ans = min(ans,diff)
        s += 1
    else:
        e += 1
print(ans)