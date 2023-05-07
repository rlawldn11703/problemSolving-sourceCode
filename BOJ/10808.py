s = input()
alpha_dict = {}
# dict 생성
for val in range(97, 123):
    alpha_dict[chr(val)]  = 0 # a ~ z
for char in s:
    alpha_dict[char] += 1
[print(count,end=" ") for count in alpha_dict.values()]