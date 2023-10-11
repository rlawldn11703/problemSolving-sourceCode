n = int(input())
cards = list(map(int,input().split()))
m = int(input())
finds = list(map(int,input().split()))
# 이분 탐색
cards.sort()
def binary_search(arr,target):
    l,r = 0,n-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return 0
ans = []
for i in range(m):
    ans.append(binary_search(cards,finds[i]))
print(*ans)