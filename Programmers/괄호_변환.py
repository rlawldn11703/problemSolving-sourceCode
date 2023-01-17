import collections
def sep(p):
    cnt_1,cnt_2 = 0,0
    for i in range(len(p)):
        if p[i] == '(': cnt_1 += 1
        else:cnt_2 += 1
        if cnt_1 == cnt_2:break
    u,v = p[:cnt_1+cnt_2],p[cnt_1+cnt_2:]
    return u,v
def ck(p):
    stack = collections.deque([p[0]])
    for i in range(1,len(p)):
        if stack[0] ==')':
            return False
        if p[i] != stack[-1]:
            stack.pop()
        else:
            stack.append(p[i])
    return True
def recur(p):
    if not p:
        return p
    u,v = sep(p)
    if ck(u):
        return u+recur(v)
    else:
        ans = '('+recur(v)+')'
        ans += ''.join([')' if i=='(' else '(' for i in u[1:-1]])
        return ans
def solution(p):
    return recur(p)
