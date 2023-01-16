n = input()
nums = list(map(int,list(n)))
ans = nums[0]
for i in range(1,len(nums)):
    if nums[i] <= 1 or ans <= 1:
        ans += nums[i]
    else:
        ans *= nums[i]
print(ans)
