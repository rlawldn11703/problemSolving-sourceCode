def check_if_prime(n):
    '''
    - 어떤 수의 소수의 여부를 확인 할 때는, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.
    - 만약, 대량의 소수를 한꺼번에 판별해야할 경우는 '에라토스테네스의 체'를 이용한다.
    '''
    arr = [1] * (n+1) # 소수를 판별할 범위만큼 배열 할당
    for i in range(2,n+1): # 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.
        if arr[i] == 0:
            continue
        for j in range(2*i,n+1,i): 
             arr[j] = 0
    prime = []
    for i in range(2,n+1): # 2부터 시작하여 남아있는 수를 모두 출력한다.
        if arr[i] != 0:
            prime.append(i)
    return prime
n = int(input())
prime = check_if_prime(n)
m = len(prime)
prime.append(0)
ans,s,e = 0,0,0
part_sum = prime[0]
while s<m and e<m:
    if part_sum == n:
        ans += 1
        s += 1
        e = s
        part_sum = prime[s]
    elif part_sum > n:
        part_sum -= prime[s]
        s += 1
    else:
        e += 1
        part_sum += prime[e]
print(ans)
# ans
s, e, ans, tmp_sum = 0, 1, 0, prime[0]
# 합의 범위 : s~e-1
while True:
    if tmp_sum == n:
        ans += 1
    if tmp_sum <= n:
        tmp_sum += prime[e]
        e += 1
    elif n < tmp_sum:
        tmp_sum -= prime[s]
        s += 1
    if e == len(prime):
        break
print(ans)