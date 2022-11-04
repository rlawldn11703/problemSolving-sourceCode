import sys
def binary_search(arr,start,end,target):
    result = 0 
    while start<=end:
        mid = (start+end)//2
        to_get = [h-mid if h-mid>0 else 0 for h in arr]
        get = sum(to_get)
        if get >= target: # 떡의 양이 충분한 경우 덜 자르기
            result = mid
            start = mid+1
        else: # 떡의 양이 부족한 경우 더 많이 자르기
            end = mid-1
    return result
n,m = map(int,input().split())
rc = list(map(int,sys.stdin.readline().rstrip().split()))
print(binary_search(rc,0,max(rc),m))
