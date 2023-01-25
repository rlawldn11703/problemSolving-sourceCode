n = int(input())
trg = []
for _ in range(n):
    trg.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(i+1):
        if j==0:
            trg[i][j] += trg[i-1][j]
        elif j==i:
            trg[i][j] += trg[i-1][j-1]
        else:
            trg[i][j] += max(trg[i-1][j],trg[i-1][j-1])
print(max(trg[-1]))
