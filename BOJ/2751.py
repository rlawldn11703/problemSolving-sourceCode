# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# Counting Sort로 해결
import sys
n = int(input())
max = 2000000
half = max//2
arr = [0] * (max+1)
for _ in range(n):
    num = int(sys.stdin.readline())
    idx = num+half
    arr[idx] += 1
for idx in range(max+1):
    if arr[idx] > 0:
        print(idx-half)

# Merge Sort로 짜보기
import sys
N = int(input())
arr = []
for _ in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
ans = []
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    low,high = merge_sort(arr[:mid]),merge_sort(arr[mid:])
    
    sorted_arr = []
    l_idx,r_idx = 0,0
    
    while l_idx < len(low) and r_idx < len(high):
        if low[l_idx] <= high[r_idx]:
            sorted_arr.append(low[l_idx])
            l_idx += 1
        else:
            sorted_arr.append(high[r_idx])
            r_idx += 1
    if l_idx < len(low): # 왼쪽 리스트 아직 남아있음
        sorted_arr.extend(low[l_idx:])
    if r_idx < len(high): # 오른쪽 리스트 아직 남아있음
        sorted_arr.extend(high[r_idx:]) 
    
    return sorted_arr
ans = merge_sort(arr)
for num in ans:
    print(num)
