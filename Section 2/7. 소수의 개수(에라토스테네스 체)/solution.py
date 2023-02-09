import sys
sys.stdin = open("/Users/ekko/Desktop/Algorithm with Python/Section 2/7. 소수의 개수(에라토스테네스 체)/input.txt", "rt")

n = int(input())

ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i]==0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt) #

