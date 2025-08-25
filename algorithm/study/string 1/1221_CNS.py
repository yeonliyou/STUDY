import sys

#다른 행성의 숫자 체계 리스트
other_num_system = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

sys.stdin = open('GNS_test_input.txt')

T = int(input())

for t in range(1, T + 1):
    # 테스트 케이스, 입력 길이 받기
    test_num, words_len = input().split()
    words_len = int(words_len)

    # 다른 행성 숫자 인풋 리스트
    input_list = input().split()  # 리스트 형태가 됨

    # 일반 숫자 체계로 바꾼 리스트
    our_num_list = []
    for other_num in input_list:
        # 다른 행성 숫자 체계 리스트에서의 인덱스가 곧 기존 숫자
        our_num = other_num_system.index(other_num)
        our_num_list.append(our_num)  # 바꾼 수 추가

    # 일반 숫자로 바꾼 리스트 오름 차순 정렬
    sorted_our_num_list = sorted(our_num_list)

    # 정렬된 리스트를 다시 다른 행성 숫자 체계로 변환
    anw = []

    # 이번엔 인덱스로 찾기
    for idx in sorted_our_num_list:
        anw.append(other_num_system[idx]) # 다시 바뀐 수 추가

    print(test_num)
    print(*anw)  #unpacking
