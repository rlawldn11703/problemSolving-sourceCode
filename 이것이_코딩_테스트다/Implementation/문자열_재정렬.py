import re
s = input()
alp,num = re.findall('[A-Z]',s),re.findall('[0-9]',s)
print(''.join(sorted(alp))+str(sum(list(map(int,num)))))
