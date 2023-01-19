import heapq
n = int(input())
min_heap = []
for _ in range(n):
    heapq.heappush(min_heap,int(input()))
ans = 0
while len(min_heap)>=2:
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    ans += (a+b)
    heapq.heappush(min_heap,a+b)
print(ans)
