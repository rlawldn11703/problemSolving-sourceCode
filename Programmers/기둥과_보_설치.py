def ck(x,y,a,dic):
    # 0은 기둥, 1은 보
    if a==0:
        if y==0 or dic[(x,y-1)][0] == True:
            return True
        if dic[(x,y)][1] == True or (x >= 1 and dic[(x-1,y)][1]==True):
            return True
        return False
    else:
        if y>= 1 and (dic[(x,y-1)][0] == True or dic[(x+1,y-1)][0]==True):
            return True
        if x>= 1 and dic[(x-1,y)][1]==True and dic[(x+1,y)][1]==True:
            return True
        return False
def solution(n, build_frame):
    cons,ans = {},[]
    for i in range(n+1):
        for j in range(n+1):
            cons[(i,j)] = [False,False]
    for build in build_frame:
        x,y,a,b = build
        # b: 0은 삭제, 1은 설치
        if b==1: 
            if ck(x,y,a,cons):
                cons[(x,y)][a] = True
                ans.append([x,y,a])
        else:
            cons[(x,y)][a]= False
            for d in ans:
                if [x,y,a] == d:
                    continue
                if not ck(d[0],d[1],d[2],cons):
                    cons[(x,y)][a] = True
                    break
            if not cons[(x,y)][a]:
                ans.remove([x,y,a])
    return sorted(ans,key=lambda x:(x[0],x[1],x[2]))
