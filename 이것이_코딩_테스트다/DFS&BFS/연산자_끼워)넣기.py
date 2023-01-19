def cal(oper,nums):
    ret = nums[0]
    for i in range(len(oper)):
        opt = oper[i]
        if opt==0:
            ret += nums[i+1]
        elif opt==1:
            ret -= nums[i+1]
        elif opt==2:
            ret *= nums[i+1]
        else:
            if ret<0:
                ret = (-ret//nums[i+1])*-1
            else:
                ret //= nums[i+1]
    return ret
n = int(input())
nums = list(map(int,input().split()))
oper = list(map(int,input().split()))
maxx,minn = -int(1e9),int(1e9)
def formula(nums,oper,arr):
    global maxx,minn,n
    if len(arr)>=n-1:
        temp = cal(arr,nums)
        maxx = max(maxx,temp)
        minn = min(minn,temp)
        return
    for i in range(4):
        if oper[i] > 0:
            arr.append(i)
            oper[i] -= 1
            formula(nums,oper,arr)
            arr.pop()
            oper[i] += 1
formula(nums,oper,[])
print(maxx);print(minn)
