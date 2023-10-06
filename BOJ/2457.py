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
        if b > s: 
            break
        if f > nxt_s:
            nxt_s = f
            max_idx = i
    # 시간 s에서 더 이상 진전이 불가능하다면
    if nxt_s == s:
        print(0)
        exit()
    ans += 1
    s = nxt_s
    idx = max_idx
print(ans)
