import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T +1 ):
    arr = []
    # 이중 리스트 만들면서, 가장 길이가 긴 인풋값 길이 저장
    max_len = 0
    for _ in range(5):
        sample = list(input()) # 문자 사이 공백 없어서 list 처리하면 쪼개짐
        arr.append(sample)
        # 현재 인풋 길이
        curr_len = len(sample)
        # 만약 현재 최대 길이보다 현재 인풋 길이가 더 길면 값 갱신
        if curr_len > max_len:
            max_len = curr_len

    anw = ''
    # 열은 max_len개로 생각하기
    for col in range(max_len):
        # 행은 5개
        for row in range(5):
            # 일단 인덱싱 시도해서 가능하면 anw에 이어붙이기
            try:
                anw += arr[row][col]
            # 해당 인덱스 값이 존재하지 않는다면 예외처리
            except:
                 continue

    print(f"#{t}", anw)





