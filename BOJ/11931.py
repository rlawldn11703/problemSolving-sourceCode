# version 1 -> 시간적 우위 (Counting Sort)
import sys
n = int(input())
max = 2000000
half = max//2
arr = [0] * (max+1)
for _ in range(n):
    num = int(sys.stdin.readline())
    idx = num+half
    arr[idx] += 1
for idx in range(max,-1,-1):
    if arr[idx] > 0:
        print(idx-half)
