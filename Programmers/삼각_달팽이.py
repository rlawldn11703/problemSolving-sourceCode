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

# 다른 방법을 이용한 풀이(그래프 탐색)
def solution(n):
    dx,dy = [0,1,-1],[1,0,-1]
    ans = [[0]*i for i in range(1,n+1)]
    x,y,num,d = 0,0,1,0
    while num <= (n*(n+1))// 2:
        ans[y][x] = num
        nx,ny = x+dx[d],y+dy[d]
        num += 1
        if 0 <= ny < n and 0<=nx<=ny and ans[ny][nx]==0:
            x,y = nx,ny
        else:
            d = (d+1) % 3 # 삼각 회전 중 다음 방향으로 넘기기
            x,y = x+dx[d],y+dy[d]
    return sum(ans,[]) # sum(iterable,start) : start를 기준으로 iterable 합치기

