def compress(s,comm,cnt):
    if cnt <= 1:
        return s+comm
    else:
        return s+str(cnt)+comm
def solution(s):
    n , ans = len(s),len(s)
    for i in range(1,len(s)//2+1):
        comm,cnt,pressed = s[:i],1,""
        for j in range(i,n-i+1,i):
            if s[j:j+i] == comm:
                cnt += 1
            else:
                pressed = compress(pressed,comm,cnt)
                comm,cnt = s[j:j+i],1
        pressed = compress(pressed,comm,cnt)
        pressed += s[j+i:]
        ans = min(ans,len(pressed))
    return ans
