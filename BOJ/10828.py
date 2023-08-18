import sys
from collections import deque
n = int(input())
stack = deque([])
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if stack: # 스택이 비어있지 않다면
            print(stack.pop())
        else: # 스택이 비어있다면 
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        # print(int(not stack))
        # 비어있을때는 0, 아니면 1이기 때문에 논리연산자 이용하기
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    