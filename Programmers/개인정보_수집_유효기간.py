# 날짜 형태 그대로 가져가도록 코드 작성
def cal_expiredate(date:list,n:int) -> list:
    '''
    만료일자 반환하는 함수
    '''
    y,m,d = date
    add_d = n*28
    year,month = 28*12,28
    add_y = add_d // year
    add_d -= year * add_y
    add_m = add_d // month
    add_d -= month * add_m
    y += add_y
    m += add_m
    d += add_d
    if d > 28:
        m += 1
        d -= 28
    if m > 12:
        y += 1
        m -= 12
    return [y,m,d]

def ck(expire_date:list,today:list) -> bool:
    '''
    expire_date가 date보다 전이면 만료. True를 반환
    '''
    for i in range(3):
        if expire_date[i] <= today[i]: # 만료
            return True
        else: 
            return False
            
def solution(today, terms, privacies):
    answer = []
    term_validtime = dict()
    today = list(map(int,today.split('.')))
    for term in terms:
        _type,validtime = term.split()
        term_validtime[_type] = int(validtime)
    for i,privacy in enumerate(privacies):
        date,t = privacy.split()
        date = list(map(int,date.split('.')))
        n = term_validtime[t]
        expire_date = cal_expiredate(date,n)
        if ck(expire_date,today):
            answer.append(i+1)
    return answer

# 날짜를 하나의 숫자로 치환하면 더 간단하게 해결가능
# 날짜에 관련된 문제 나오면 하나의 숫자로 치환하는 방법 생각하기
def to_days(date:str):
    y,m,d = map(int,date.split('.'))
    return y*28*12 + m*28 + d
  
def solution_2(today, terms, privacies):
    answer = []
    term_validtime = dict()
    today = to_days(today)
    for term in terms:
        _type,validtime = term.split()
        term_validtime[_type] = int(validtime)
    for i,privacy in enumerate(privacies):
        date,t = privacy.split()
        n = term_validtime[t]
        expire_date = to_days(date) + n*28
        if expire_date <= today:
            answer.append(i+1)
    return answer
