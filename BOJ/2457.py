# 그리디한 관점에서 생각해보면 매번 현재 시점에서 피어있는 꽃 중에서 가장 마지막에 지는 꽃 선택
# 만약 1일에서 1,000,000,000일 사이에서 꽃들을 정해야 하는 문제라면?
# 현재 풀이 그대로는 시간 초과일텐데 어떻게 해결해야할까?
n = int(input())
flower = []
for _ in range(n):
    s_m,s_d,e_m,e_d = map(int,input().split())
    flower.append((s_m*100+s_d,e_m*100+e_d))
# 꽃이 빨리 피고, 늦게 지는 순으로 정렬! 
flower.sort(key=lambda x:(x[0],-x[1]))
s,e = 301,1201
idx,ans = 0,0
nxt_s = s
while s < e:
    for i in range(idx,n):
        b,f = flower[i]
        # 시작일 이후에 꽃이 피면 의미없음 
        if b > s: 
            break
        # 가장 늦게 지는 꽃 찾기
        if f > nxt_s:
            nxt_s = f
            idx = i
    # 시간 s에서 더 이상 진전이 불가능하다면
    if nxt_s == s:
        print(0)
        exit()
    # 꽃 선택 가능하다면
    ans += 1
    s = nxt_s
print(ans)
