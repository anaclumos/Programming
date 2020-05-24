# N개의 상자
# 1 <= l <= m < r <= N

# (1 <= l <= m, m+1 <= r <= N)

# l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 

def getCookieOf(cookie, l, m, r):
    sonone = cookie[l-1:m]
    sontwo = cookie[m:r]
    # print(sonone)
    # print(sontwo)
    if sum(sonone) == sum(sontwo):
        return sum(sonone)
    else:
        return 0

def solution(cookie):
    N = len(cookie)
    answer = 0
    for l in range(1, N):
        for r in range(l+1, N+1):
            # print(l, m, r)
            a = getCookieOf(cookie, l, m, r)
            if a > answer:
                answer = a
    return answer

cookie = [1,2,4,5]

print(solution(cookie))