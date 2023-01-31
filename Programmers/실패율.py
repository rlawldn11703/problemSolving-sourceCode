def solution(n,stages):
    fail,result = [0]*(n+1),[0]*n
    for s in stages:
        fail[s-1] += 1
    clear = sum(fail)
    for i in range(n):
        if clear == 0:
            result[i] = (i+1,0)
        else:
            result[i] = (i+1,fail[i]/clear)
        clear -= fail[i]
    result.sort(key=lambda x:x[1],reverse=True)
    return [idx for idx,_ in result]
