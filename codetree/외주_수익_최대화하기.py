n = int(input())
works = []
ans = 0
for i in range(n):
    t,p = map(int,input().split())
    works.append((i+t-1,p))
print(works)
def maximize_revenue(start,revenue):
    global ans
    if start >= n:
        return
    for i in range(start,n):
        end_date,p = works[i]
        if end_date < n:
            ans = max(ans,revenue+p)
        maximize_revenue(end_date+1,revenue+p)
maximize_revenue(0,0)
print(ans)
        
