from collections import defaultdict
n = int(input())
# linked list version
for _ in range(n):
    s = input()
    cnt = defaultdict(int)
    linked_list = {} # 문자끼리의 순서
    linked_list['start'] = [None,'end']
    linked_list['end'] = ['start',None]
    cursor = 'start' # 커서 왼쪽에 위치한 문자
    for cmd in s:
        if cmd == '-': # 바로 앞에 글자 삭제
            if cursor != 'start':
                prev,next = linked_list[cursor][0],linked_list[cursor][1]
                if prev:
                    linked_list[prev][1] = next
                if next:
                    linked_list[next][0] = prev
                del linked_list[cursor]
                cursor = prev
        elif cmd == '<':
            if cursor != 'start':
                cursor = linked_list[cursor][0]
        elif cmd == '>':
            if linked_list[cursor][1] != 'end':
                cursor = linked_list[cursor][1]
        else: # cmd == 대문자,소문자,숫자
            cnt[cmd] += 1
            cmd = cmd + str(cnt[cmd])
            prev,next = linked_list[cursor][0],linked_list[cursor][1]
            linked_list[cursor][1] = cmd
            linked_list[next][0] = cmd
            linked_list[cmd] = [cursor,next]
            cursor = cmd
    node = 'start'
    while node != 'end': # 계속 next 찾아서 뽑아내기
        if node != 'start': # start가 아니라면
            print(node[0],end='')
        node = linked_list[node][1]
    print()
# stack version
# 1
for _ in range(n):
    s = input()
    left,right = [],[]
    for cmd in s:
        if cmd == '-': # 바로 앞에 글자 삭제
            if left:
                left.pop()
        elif cmd == '<':
            if left:
                right.append(left.pop())
        elif cmd == '>':
            if right:
                left.append(right.pop())
        else: # cmd == 대문자,소문자,숫자
            left.append(cmd)
    print(''.join(left+right[::-1]))
# 2
from collections import deque
n = int(input())
for _ in range(n):
    s = input()
    left,right = deque([]),deque([])
    for cmd in s:
        if cmd == '-': # 바로 앞에 글자 삭제
            if left:
                left.pop()
        elif cmd == '<':
            if left:
                right.appendleft(left.pop())
        elif cmd == '>':
            if right:
                left.append(right.popleft())
        else: # cmd == 대문자,소문자,숫자
            left.append(cmd)
    print(''.join(left+right))
