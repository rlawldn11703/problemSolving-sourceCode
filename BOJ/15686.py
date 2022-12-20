from itertools import combinations
def cal_dist(home,chicken):
    chicken_dist = 0
    for h in home:
        dist = int(1e9)
        for c in chicken:
            dist = min(dist,abs(h[0]-c[0])+abs(h[1]-c[1]))
        chicken_dist += dist
    return chicken_dist
n,m = map(int,input().split())
Map = []
for _ in range(n):
    Map.append(input().split())
home,chicken,ans = [],[],int(1e9)
for i in range(n):
    for j in range(n):
        if Map[i][j]=='1':
            home.append((i,j))
        elif Map[i][j]=='2':
            chicken.append((i,j))
for selected in combinations(chicken,m):
    ans = min(ans,cal_dist(home,selected))
print(ans)
    
