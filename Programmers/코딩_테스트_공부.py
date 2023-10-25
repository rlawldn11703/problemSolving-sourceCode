def ck_range(x,y,max_al,max_co):
    x = min(x,max_al)
    y = min(y,max_co)
    return x,y

def solution(dic):
    '''
    dp[i][j]: 알고력 i와 코딩력 j를 얻을 수 있는 최단 시간
    '''
    alp = dic['alp'] 
    cop = dic['cop'] 
    problems = dic['problems'] 
    
    max_size = int(1e6)
    max_al = max(problems,key=lambda x:x[0])[0]
    max_co = max(problems,key=lambda x:x[1])[1]
    alp = min(alp,max_al)
    cop = min(cop,max_co)
    
    # dp table 초기화
    dp = [[max_size]* (max_co+1) for _ in range(max_al+1)]
    dp[alp][cop] = 0
            
    for al in range(alp,max_al+1):
        for co in range(cop,max_co+1):
            for x,y in [(al+1,co),(al,co+1)]:
                x,y = ck_range(x,y,max_al,max_co)
                dp[x][y] = min(dp[x][y], dp[al][co]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if al >= alp_req and co >= cop_req:
                    x,y = ck_range(al+alp_rwd,co+cop_rwd,max_al,max_co)
                    dp[x][y] = min(dp[x][y],dp[al][co]+cost)    
    return dp[-1][-1]
