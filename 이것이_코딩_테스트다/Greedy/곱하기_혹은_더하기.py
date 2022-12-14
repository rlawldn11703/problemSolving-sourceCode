n = input()
nums = list(map(int,list(n)))
ans = 1
for num in nums:
    if num != 0:
        ans *= num
print(ans)
