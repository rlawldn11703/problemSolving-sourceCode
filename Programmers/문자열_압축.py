def solution(s):
    ans = len(s)
    for i in range(1,len(s)//2+1):
        press,cnt,j = "",1,0
        for j in range(0,len(s),i):
            common = s[j:j+i]
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
            else:
                if cnt >1 :
                    press += str(cnt) + common
                else:
                    press += common
                cnt = 1
        ans = min(ans,len(press))
    return ans
