import sys
n = int(sys.stdin.readline())
start = 1 # start부터 넣을 수 있음.
stack, cmd = [],[]
for _ in range(n):
    num =  int(sys.stdin.readline())
    while start <= num :
        stack.append(start)
        cmd.append('+')
        start += 1
    while stack and stack[-1] >= num:
        last_pop = stack.pop()
        cmd.append('-')
    if last_pop != num:
        print('NO')
        exit(0)
[print(c) for c in cmd]

# answer
n = int(input())
S = []
cnt = 1
ans = []
for _ in range(n):
    t = int(input())
    while cnt <= t:
        S.append(cnt)
        ans.append("+")
        cnt += 1
    if S[-1] != t:
        print("NO")
        exit(0)
    S.pop()
    ans.append("-")

for symbol in ans:
    print(symbol)
