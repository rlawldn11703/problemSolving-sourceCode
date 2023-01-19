n = int(input())
dist = sorted(list(map(int,input().split())))
print(dist[(n-1)//2])
