# 이진탐색
def binary_search(arr,start,end,target):
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 'yes'
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 'no'
n =int(input())
product = sorted(list(map(int,input().split())))
m = int(input())
req = list(map(int,input().split()))
for i in range(m):
    print(binary_search(product,0,n-1,req[i]),end = ' ')

# 계수정렬
n =int(input())
product = [0]*1000001
for i in input().split():
    product[int(i)] = 1
m = int(input())
req = list(map(int,input().split()))
for i in range(m):
    if product[req[i]] == 1:
        print('yes',end = ' ')
    else:
        print('no',end = ' ')
        
# 집합 자료형 이용
n =int(input())
product = set(map(int,input().split()))
m =int(input())
req = list(map(int,input().split()))
for i in range(m):
    if req[i] in product:
        print('yes',end = ' ')
    else:
        print('no',end = ' ')
