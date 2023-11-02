import sys

sys.stdin = open("/Users/ekko/Desktop/Algorithm-Python/Section3/5. 수들의 합/input.txt", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0 
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)