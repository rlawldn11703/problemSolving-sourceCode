# brute-force로 하다가 시간 오버된 경우 -> dp로 해결해보기
# 1. dp
# 2. 투포인터 
# 3. 이분탐색
# 4. 그리디 시도해보기
# dp[i][j] = i분 상태의 j도 만들어낼 수 있는 에어컨의 소비전력
def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1,t2 = t1+10,t2+10
    n,m = len(onboard),51
    maxsize = int(1e6)
    dp = [[maxsize]*m for _ in range(n)]
    dp[0][temperature] = 0
    def find_mincost(i,now,prev,c):
        nonlocal dp
        if now < 0 or now > 50:
            return
        dp[i+1][now] = min(dp[i+1][now],dp[i][prev]+c)
    # dp로 풀게될 경우 O(nm) - > 51*1000
    for i in range(n-1):
        # 승객이 타 있다면 t1에서 t2 사이에 있는 j값에서만 이동 가능
        # t1에서 t2 구간 밖에 있는 온도들은 불가능한 경우
        s,e = (t1,t2+1) if onboard[i] == 1 else (0,m)
        for j in range(s,e):
            # 끄고 외부온도 방향으로 1 이동
            if temperature > j:
                move = 1
            elif temperature < j:
                move = -1
            else:
                move = 0
            find_mincost(i,j+move,j,0)
            # 켜고 현재온도 유지
            find_mincost(i,j,j,b)
            # 켜고 온도 1 증가 or 감소
            find_mincost(i,j+1,j,a)
            find_mincost(i,j-1,j,a)
    # 원하는 값 출력
    s,e = (t1,t2+1) if onboard[-1] == 1 else (0,m)
    ans = int(1e9)
    for j in range(s,e):
        if dp[-1][j] != maxsize:
            ans = min(ans,dp[-1][j])
    return ans
temperature,t1,t2,a,b = 11,8,10,10,100
onboard = 	[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
print(solution(temperature,t1,t2,a,b,onboard))