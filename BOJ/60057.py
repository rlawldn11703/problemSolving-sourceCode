score = list(map(int,list(input())))
n = len(score)
if sum(score[:n//2])==sum(score[n//2:]):
    print('LUCKY')
else:
    print('READY')
