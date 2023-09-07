left,right = list(input()),[]
M = int(input())
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])
full = left + right[::-1]
print(''.join(full))

# answer
init = input().strip()
L = list(init)
cursor = len(L)
q = int(input())
for _ in range(q):
    op = input().split()
    if op[0] == 'P':
        add = op[1]
        L.insert(cursor, add)
        cursor += 1
    elif op[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif op[0] == 'D':
        if cursor < len(L):
            cursor += 1
    else:  # 'B'
        if cursor > 0:
            del L[cursor - 1]
            cursor -= 1
print(''.join(L))
