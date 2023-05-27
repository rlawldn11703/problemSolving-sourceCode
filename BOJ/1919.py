count_1,count_2 = [0] * 26, [0] * 26
s1, s2 = input(), input()
for s in s1:
    count_1[ord(s)-ord('a')] += 1
for s in s2:
    count_2[ord(s)-ord('a')] += 1
ans = 0
for i in range(len(count_1)):
    if count_1[i] != count_2[i]:
        ans += abs(count_1[i] - count_2[i])
print(ans)
