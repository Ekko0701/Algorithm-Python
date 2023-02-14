import sys
sys.stdin = open("/Users/ekko/Desktop/Algorithm with Python/Section3/1. 회문 문자열 검사/input.txt", 'r')
n = int(input())

for i in range(n):
    s = input()
    s=s.upper()
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))