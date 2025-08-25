import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    # 단어 퍼즐의 가로, 세로길이 / 단어의 길이 K
    N , K = map(int, input().split())

    # 가로 체크
    
    # 세로 체크