# 수업을 빨리 시작하는 순으로 정렬
# 우선순위 큐를 이용해 빈 강의실이 없는 경우 강의실을 하나 추가하는 방식으로 구현
import heapq,sys
n = int(input())
classes = []
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    classes.append((s,e))
# 수업 빨리 시작하는 순으로 정렬
classes.sort(key=lambda x:x[0])
ans,room = 1,[0]
heapq.heapify(room)
for s,e in classes:
    if s < room[0]: # 수업 시작 가능한 교실이 없음
        ans += 1
    else: # 수업 시작 가능
        heapq.heappop(room)
    heapq.heappush(room,e)
print(ans)

# ans
# 문제의 답은 결국 가장 많은 수업이 열리는 시간에서의 수업의 개수이다.
# 수업 개수의 변화가 발생하는 (s, 1), (t, -1)을 전부 수집한 후 정렬하고 같은 시간대의 event를 묶어서 처리한다.
n = int(input())
event = []
for _ in range(n):
    s, t = map(int, input().split())
    event.append((s, 1))
    event.append((t, -1))
event.sort()

ans = 0 # 필요한 강의실의 최대 개수
curtime = event[0][0] # 현재 시간
cur = 0 # 현재 시간에 열려있는 강의실의 개수
idx = 0 # 현재 보고있는 event에서의 인덱스

while True:
    # 해당 시간에 벌어지는 일 모두 계산
    while idx < 2 * n and event[idx][0] == curtime:
        cur += event[idx][1]
        idx += 1
    ans = max(ans, cur)
    if idx == 2 * n:
        print(ans)
        exit()
    # 다음 이벤트가 일어나는 시간
    curtime = event[idx][0]
