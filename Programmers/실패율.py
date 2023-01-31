def solution(n,stages):
    fail,result = [0]*(n+1),[0]*n
    for s in stages:
        fail[s-1] += 1
    clear = sum(fail)
    for i in range(n):
        if clear == 0:
            result[i] = (0,i+1)
        else:
            result[i] = (fail[i]/clear,i+1)
        clear -= fail[i]
    result.sort(key=lambda x:(x[0],-x[1]),reverse=True)
    return [idx for x,idx in result]
