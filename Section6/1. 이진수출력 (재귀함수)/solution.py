import sys
sys.stdin = open("/Users/ekko/Desktop/Algorithm-Python/Section6/1. 이진수출력 (재귀함수)/input.txt", 'r')

def DFS(x): 
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__  == "__main__":
    n = int(input())
    DFS(n)