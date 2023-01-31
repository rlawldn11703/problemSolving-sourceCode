n,x = map(int,input().split())
arr = list(map(int,input().split()))
def bileft(arr,n,x): #x보다 작은 수가 처음 등장
    left,right = 0,n-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] >= x:
            right = mid-1
        else:
            left = mid+1
    return left
def biright(arr,n,x): #x보다 큰 수가 처음 등장
    left,right = 0,n-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]>x:
            right = mid-1
        else:
            left = mid+1
    return left
l,r = bileft(arr,n,x),biright(arr,n,x)
if r-l==0:
    print(-1)
else:
    print(r-l)
