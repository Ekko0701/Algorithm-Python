arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 파이썬에서 가장 큰수로 초기화됨.

for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]

print(arrMin)