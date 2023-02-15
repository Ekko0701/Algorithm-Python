import sys
sys.stdin = open("/Users/ekko/Desktop/Algorithm with Python/Section3/2. 숫자만 추출/input.txt", 'r')
n = input()

### 1번 
# resultStr = ''
# count = 0

# for i in n: 
#     if i.isdigit(): 
#         resultStr += i



# result = int(resultStr)
# print(result)

# for i in range(1, result + 1):
#     if (result % i == 0): 
#         count += 1

# print(count)
  
### 2번
result = 0
count = 0

for i in n:
    if i.isdecimal():
        result = result * 10 + int(i)
print(result)

for i in range(1, result + 1):
    if result % i == 0:
        count += 1
print(count)