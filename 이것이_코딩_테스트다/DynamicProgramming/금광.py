T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    Board = [[] for _ in range(n)]
    for i in range(0,len(arr),m):
        Board[i//m] = arr[i:i+m]
    dx = [-1,0,1]
    for y in range(1,m):
        for x in range(n):
            maxx = -1
            for w in range(3):
                nx = x+dx[w]
                if 0<=nx<n:
                    maxx = max(maxx,Board[nx][y-1])
            Board[x][y] += maxx
    ans = -1
    for x in range(n):
        ans = max(ans,Board[x][-1])
    print(ans)
