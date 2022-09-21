n,ans = int(input()),0
def ck(num):
    if '3' in str(num):
        return True
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if ck(h) or ck(m) or ck(s):
                ans += 1
print(ans)
