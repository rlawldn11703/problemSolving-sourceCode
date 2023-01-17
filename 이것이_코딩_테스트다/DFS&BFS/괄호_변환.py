def divide(p):
    cnt = [0,0]
    for i in range(len(p)):
        if p[i]=='(': cnt[0] += 1
        else: cnt[1] += 1
        if cnt[0]==cnt[1]:
            return p[:i+1],p[i+1:]
def ck(w):
    stack = []
    for i in w:
        if not stack or i=='(':
            stack.append(i)
        elif stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0: return True
    else:
        return False
def solution(p):
    if len(p)==0:
        return p
    u,v = divide(p)
    if ck(u):
        return u+solution(v)
    else:
        ret = '('
        ret += solution(v)
        ret += ')'
        for i in range(1,len(u)-1):
            if u[i]=='(':ret += ')'
            else: ret += '('
        return ret
