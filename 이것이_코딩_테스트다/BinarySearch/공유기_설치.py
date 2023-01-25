n,c = map(int,input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()
left,right,result = 1,home[-1]-home[0],0
while left<=right:
    mid = (left+right)//2
    value = home[0]
    count = 1
    for i in range(1,n):
        if home[i]>=value+mid:
            value = home[i]
            count += 1
    if count >= c:
        left = mid+1
        result = mid
    else:
        right = mid-1
print(result)
