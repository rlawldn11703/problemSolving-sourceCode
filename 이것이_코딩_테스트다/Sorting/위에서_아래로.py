# 기본 정렬 라이브러리 
import sys
n,arr = int(input()),[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort(reverse=True)
[print(i,end=' ') for i in arr]

# 계수 정렬 
n,arr = int(input()),[0]*100001
for _ in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1
for idx in range(len(arr)-1,0,-1):
    if arr[idx] != 0:
        [print(idx,end=' ') for _ in range(arr[idx])]
