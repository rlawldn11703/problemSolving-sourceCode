from itertools import combinations
def cal_intensity(arr):
    intensity = 0
    for i,j in combinations(arr,2):
        add = board[i][j] + board[j][i]
        intensity += add
    return intensity

n = int(input())
board = []
for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)

ans = int(1e9)
for combi in combinations(list(range(n)),n//2):
    # n//2 개 고르는 조합
    rest = set(range(n))
    for m in combi:
        rest.remove(m)
    morn = cal_intensity(combi) # 아침에 하는 일 업무강도
    night = cal_intensity(rest) # 저녁에 하는 일 업무강도
    ans = min(ans,abs(morn-night))
print(ans)
