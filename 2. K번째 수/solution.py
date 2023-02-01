import sys
sys.stdin = open("input.txt", "rt")

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a = a[s-1:e] # s-1 ~ e-1 인덱스 슬라이싱
    a.sort() # 오름차순 정렬

    print("#%d %d" %(t+1, a[k-1]))