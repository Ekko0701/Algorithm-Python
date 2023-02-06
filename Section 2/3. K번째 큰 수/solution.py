import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))

res = set() # Set으로 중복 제거

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res) # Set에는 정렬 메소드를 사용할 수 없기에 다시 리스트로 바꿔주었다.

res.sort(reverse=True) # 내림차순으로 정렬

print(res[k-1])