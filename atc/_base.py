import sys
input = sys.stdin.readline
INF = 1 << 30
N = int(input())
N, M = map(int, input().split())
A, B = map(lambda x:int(x)-1, input().split())
As = list(map(int, input().split()))