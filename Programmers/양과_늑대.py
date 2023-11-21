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
    def dfs(graph,info,to_visit,cnt):
        nonlocal answer
        if cnt[0]<= cnt[1]:
            return 
        answer = max(answer,cnt[0])
        for now in to_visit:
            next_visit = deepcopy(to_visit)
            next_visit.remove(now)
            next_visit.update(graph[now])
            cnt[info[now]] += 1
            dfs(graph,info,next_visit,cnt)
            cnt[info[now]] -= 1
    dfs(graph,info,to_visit,[1,0])
    return answer
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))