def cal_emoticonplus(ratio:list,users:list,emoticons:list):
    cnt,sales = 0,0 # 가입자수, 판매액
    for want,budget in users:
        buy = 0
        for r,emoticon in zip(ratio,emoticons):
            if r >= want : # 원하는 할인폭보다 크면
                buy += (100-r)*emoticon//100
        if buy >= budget:
            cnt += 1
        else:
            sales += buy
    return cnt,sales  
def solution(users, emoticons):
    p = [10,20,30,40]
    n = len(emoticons)
    ans = [0,0]
    for tmp in range(4**n):
        brute = tmp
        sale_ratio = []
        for _ in range(n):
            idx = brute % 4
            brute //= 4
            sale_ratio.append(p[idx])
        cnt,sales = cal_emoticonplus(sale_ratio,users,emoticons)
        if cnt > ans[0] or (cnt == ans[0] and sales > ans[1]):
            ans = [cnt,sales]
    return ans
# itertools에 product 사용할수도 있음! (데카르트 곱 : cartesian product)
from itertools import product
def solution(users, emoticons):
    p = [10,20,30,40]
    n = len(emoticons)
    ans = [0,0]
    for sale_ratio in product(p,n):
        cnt,sales = cal_emoticonplus(sale_ratio,users,emoticons)
        if cnt > ans[0] or (cnt == ans[0] and sales > ans[1]):
            ans = [cnt,sales]
    return ans