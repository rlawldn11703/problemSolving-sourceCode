def solution(n):
    ans = [0] * ((n*(n+1))//2)
    idx,num,h = 0,1,0
    for i in range(n,0,-1):
        j = n-i
        if j%3 == 0:
            for _ in range(i):
                idx += h
                ans[idx] = num
                num, h = num+1 , h+1
        elif j%3 == 1:
            for _ in range(i):
                idx += 1
                ans[idx] = num
                num += 1
        else:
            for _ in range(i):
                idx -= h
                ans[idx] = num
                num , h = num+1,h-1
    return ans
