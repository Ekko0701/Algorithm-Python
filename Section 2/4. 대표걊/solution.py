import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a) / n)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min: 
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)


# 추가 
# Python에서 Round 메서드는 round_half_even 방식을 택한다
# 정확히 절반 (5) 인 경우에 round를 하면 짝수 쪽으로 반올림 된다.
# ex) 
# round(4.5) -> 4
# round(4.51) -> 5 

# 해결법
# 소수점 첫번째 자리까지만 고려하니
# 소수점 첫번째 자리가 5 이상이면 0.5를 더해주자
# ex)
# a = 66.5
# a = a + 0.5 
# 이렇게 하면 기존에 알던 반올림 방식으로 작동한다.