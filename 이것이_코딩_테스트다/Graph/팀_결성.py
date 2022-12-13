n,m = map(int,input().split())
team = [i for i in range(n+1)]
def find(parents,x):
    if parents[x] != x:
        parents[x] = find(parents,parents[x])
    return parents[x]
for _ in range(m):
    opt,a,b = map(int,input().split())
    par_a,par_b = find(team,a),find(team,b)
    if opt==0:
        team[max(par_a,par_b)] = min(par_a,par_b)
    elif opt==1:
        if par_a == par_b:
            print('YES')
        else:
            print('NO')
