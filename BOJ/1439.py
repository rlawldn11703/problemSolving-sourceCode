num = input()
sec= [0,0]
sec[int(num[0])] += 1
for i in range(len(num)-1):
    if num[i] != num[i+1]:
        sec[int(num[i+1])] += 1
print(min(sec))
