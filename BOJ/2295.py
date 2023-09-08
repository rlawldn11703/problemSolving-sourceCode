N = int(input())
arr = []
def binary_search(target,arr):
    left,right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

for _ in range(N):
    num = int(input())
    arr.append(num)
arr.sort()

sum_of_two = []
for i in range(N):
    for j in range(i,N):
        sum_of_two.append(arr[i]+arr[j])
sum_of_two.sort()

for i in range(N-1,-1,-1):
    # 세수의 합 후보
    target = arr[i]
    for j in range(N):
        if binary_search(target-arr[j],sum_of_two):
            print(arr[i])
            exit()
