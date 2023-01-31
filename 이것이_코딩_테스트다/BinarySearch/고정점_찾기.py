n = int(input())
arr = list(map(int,input().split()))
left,right,ck = 0,n-1,False
while left<=right:
    mid = (left+right)//2
    if arr[mid]==mid:
        print(mid)
        ck = True
        break
    elif arr[mid] > mid:
        right = mid-1
    else:
        left = mid+1
if ck==False:
    print(-1)
