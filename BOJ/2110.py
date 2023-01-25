n,c = map(int,input().split())
home = []
for _ in range(n):
    home.append(int(input()))
home.sort()
def dist(num,c):
    idx,cnt = 0,1
    for i in range(1,len(home)):
        if home[i]-home[idx]>=num:
            cnt += 1
            idx = i
    if cnt >= c:
        return True
    else:
        return False
left,right,result = 1,home[-1]-home[0],0
while left<=right:
    mid = (left+right)//2
    if dist(mid,c):
        left = mid+1
        result = mid
    else:
        right = mid-1
print(result)
