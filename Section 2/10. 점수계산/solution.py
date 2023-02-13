import sys
sys.stdin = open("/Users/ekko/Desktop/Algorithm with Python/Section 2/10. 점수계산/input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

sum = 0 
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else: 
        cnt = 0
        
print (sum)