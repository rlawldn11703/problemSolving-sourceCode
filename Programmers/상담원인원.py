import heapq
def waiting_time(req,num):
    '''
    유형별 req, mentor수에 따라 기다리는 시간 계산하는 함수
    '''
    if len(req) <= num: # 멘토의 수가 멘티의 수보다 많을때 기다리지 않아도 된다! 
        return 0
    waiting = 0
    mentor = [0] * num
    heapq.heapify(mentor)
    for start,dur in req:
        # 가장 빨리 가능한 멘토
        avail = heapq.heappop(mentor) # 가장 빨리 상담 시작가능한 시간
        if start < avail: # 상담 가능한 멘토가 없다면
            waiting += (avail-start)
            heapq.heappush(mentor,avail+dur)
        else: # 요청 즉시 상담을 시작할 수 있다면
            heapq.heappush(mentor,start+dur)
    return waiting

def solution(k, n, reqs):
    '''
    using dfs : 시간적 측면에서 이득
    '''
    req_type = [[] for _ in range(k+1)]
    for req in reqs:
        start,dur,t = req
        req_type[t].append((start,dur))
    # 유형별로 멘토 나눠서 대기 시간 확인하기
    answer = int(1e9)
    def noc(cnt,avail_m,total_wait):
        nonlocal answer
        if cnt == k+1:
            answer = min(answer,total_wait)
            return
        for num in range(avail_m+1):
            wait = waiting_time(req_type[cnt],num+1)
            noc(cnt+1,avail_m-num,total_wait+wait)
    noc(1,n-k,0)
    return answer

def solution(k, n, reqs):
    '''
    using for loop -> 각 멘토당 1~n-k+1까지 모두 계산하기 때문에 시간 복잡도 높음
    '''
    req_type = [[] for _ in range(k+1)]
    for req in reqs:
        start,dur,t = req
        req_type[t].append((start,dur))
    # 유형별로 멘토 나눠서 대기 시간 확인하기
    answer = int(1e9)
    dm = n-k+1 # 경우의 수
    for tmp in range(dm**k):
        brute = tmp
        m = [0] * (k+1)
        for i in range(k):
            m[i+1] = brute % dm + 1
            brute //= dm
        if sum(m) == n:
            total_wait = 0
            for t in range(1,k+1):
                total_wait += waiting_time(req_type[t],m[t])
            answer = min(answer,total_wait)
    return answer
