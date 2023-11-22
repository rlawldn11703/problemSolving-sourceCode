from collections import defaultdict
from copy import deepcopy
def solution(info, edges):
    graph = defaultdict(list)
    answer = 0
    for edge in edges:
        parent,child = edge
        graph[parent].append(child)
    to_visit = set()
    to_visit.update(graph[0])
    def dfs(to_visit,cnt):
        nonlocal answer
        if cnt[0]<= cnt[1]:
            return 
        answer = max(answer,cnt[0])
        for now in to_visit:
            next_visit = deepcopy(to_visit)
            next_visit.remove(now)
            next_visit.update(graph[now])
            cnt[info[now]] += 1
            dfs(next_visit,cnt)
            cnt[info[now]] -= 1
    dfs(to_visit,[1,0])
    return answer